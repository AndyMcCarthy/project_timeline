import React, { useEffect, useRef, useState } from "react";
import { DataSet } from "vis-data";
import { Timeline } from "vis-timeline/standalone";
import Document from "./Document.png"
import clinicaltrial from "./clinicaltrial.png"
import scientificpaper from "./scientificpaper.png"
import './timeline.css'

export const VisTimeline = () => {
	const [timelineData, setTimelineData] = useState([]);

	const [open, setOpen] = useState(false);
	//const [datasetItems, setDatasetItems] = useState(new DataSet());
	const [editedItem, setEditedItem] = useState({ content: '', className: '', type: '', URL: '', image: '', displayName:'', edited: false });
	const [editedCallback, setEditedCallback] = useState('');
	//const [deletedItems, setDeletedItems] = useState([]);

	const fetchData = async () => {
		try {
			const response = await fetch("/api/timeline");
			const data = await response.json();
			setTimelineData(data);
		} catch (error) {
			console.error("Error fetching timeline data:", error);
		}
	};

	const visJsContainer = useRef(null);

	const imageSelection = (image_type) => {
		if (image_type === 1) {
			return Document
		}
		if (image_type === 2) {
			return scientificpaper
		}
		if (image_type === 3) {
			return clinicaltrial
		}

		return Document


	}

	function isValidUrl(string) {
		try {
			var url = new URL(string);
			return url.protocol === 'http:' || url.protocol === 'https:';
		} catch (err) {
			return false;
		}
	}

	function escapeXml(unsafe) {
		return unsafe.replace(/[<>&'"]/g, function (c) {
			switch (c) {
				case '<': return '&lt;';
				case '>': return '&gt;';
				case '&': return '&amp;';
				case '\'': return '&apos;';
				case '"': return '&quot;';
			}
		});
	}

	const handleUpdate = (event, reason) => {
		if (reason === 'backdropClick' || reason === 'escapeKeyDown') {
		  return;
		}
		// do some error handling to prevent mistakes...
		//also set classname so colour matches group
		let newcontent = `<img src='${imageSelection(editedItem.group)}' style='width: 28px; height: 28px;'>`;
	  
		if (editedItem.hasOwnProperty('hyperlink')) {
		  if (editedItem.hyperlink === "") {
			newcontent += ` ${editedItem.displayName}`;
		  } else if (isValidUrl(editedItem.hyperlink)) {
			newcontent += ` <a href="${escapeXml(editedItem.hyperlink)}" target="_blank">${editedItem.displayName}</a>`;
		  } else {
			alert(editedItem.hyperlink + " is not a valid URL");
			return;
		  }
		} else {
		  newcontent += ` ${editedItem.displayName}`;
		}
	  
		editedItem.content = newcontent;
		setOpen(false);
		editedCallback(editedItem);
	  };

	const handleClose = (event, reason) => {
		setOpen(false);
	};
	
	useEffect(() => {
		fetchData();
	}, []); // Run only once when the component mounts to fetch initial data

	useEffect(() => {
		// Check if timelineData has data before proceeding
		if (timelineData.length === 0) return;

		const datasetItems = new DataSet([]);
		timelineData.map(event => {
			const this_event = {
				id: event.Id,
				group: event.group,
				content: `<img src='${imageSelection(event.group)}' style='width: 28px; height: 28px;'> <a href=${event.hyperlink} target="_blank">${event.displayName}</a> `,
				editable: event.editable,
				type: event.type,
				className: event.className,
				start: event.start,
				end: event.end || event.start,
				title: event.title,
				hyperlink: event.hyperlink,
				displayName: event.displayName
			};
			datasetItems.add(this_event);
		});

		const groups = new DataSet([
			{ id: 3, content: "Clinical Trials" },
			{ id: 1, content: "Patents" },
			{ id: 2, content: "Papers" },

		]);

		const today = new Date();
		const options = {
			width: '100%',
			start: '2010-01-01',
			end: new Date().setFullYear(today.getFullYear() + 1),
			editable: true,
			tooltip: {
				followMouse: true,
				template: function (originalItemData, parsedItemData) {
					//console.log(originalItemData)
					return `<div style="max-width:300px; word-wrap:break-word;">
							<p>${originalItemData.content}</p>${(originalItemData.title == null) ? '' : `<p id="para1">${originalItemData.title} </p>`}
						</div>
				`;
					//return ReactDOM.render(<b>{originalItemData.content}</b>, parsedItemData);
				},
			},
			onUpdate: function (item, callback) {
				//clone item
				setEditedItem({ ...item })
				//clone callback
				setEditedCallback(() => callback)
				setOpen(true)
			},
			onMove(item, callback) {
				//Change content to reflect new group/classname
				//also set classname so colour matches group
				item.edited = true
				callback(item);
			},
			onRemove: function (item, callback) {
				//setDeletedItems(deletedItems => [...deletedItems, item.id]);
				callback(item);
			},
		};

		const timeline = visJsContainer.current && new Timeline(visJsContainer.current, datasetItems, groups, options);

		// Cleanup function to destroy the timeline when the component unmounts
		return () => {
			if (timeline) {
				timeline.destroy();
			}
		};
	}, [timelineData]);

	return (
		<>
			<div ref={visJsContainer} />

			{open ?
				<div className="popup">
					<div className="popup-inner">
						<form open={open} onSubmit={handleUpdate} >
							<h2>Edit item</h2>
							<label> Edit items name:
								<input name="content" value={editedItem.displayName} onChange={(event) => setEditedItem({ ...editedItem, "displayName": event.target.value })} />
							</label>
							<label> Edit items URL:
								<input name="hyperlink" value={editedItem.hyperlink} onChange={(event) => setEditedItem({ ...editedItem, "hyperlink": encodeURI(event.target.value) })} />
							</label>
							<label> Edit items description:
								<textarea name="title" value={editedItem.title} onChange={(event) => setEditedItem({ ...editedItem, "title": event.target.value })} />
							</label>
							<button onClick={event => handleClose(event, "update")} >
								Cancel
							</button>
							<button onClick={event => handleUpdate(event, "close")} >
								Update
							</button>

						</form>
					</div>
				</div>
				: null}

		</>
	);
};