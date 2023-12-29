import React, { useEffect, useRef, useState} from "react";
import {DataSet} from "vis-data";
import { Timeline } from "vis-timeline/standalone";
import Document from "./Document.png"
import clinicaltrial from "./clinicaltrial.png"
import './timeline.css'

export const VisTimeline = () => {
  const [timelineData, setTimelineData] = useState([]);

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

  const imageSelection = (image_type) =>{
    console.log(image_type)
    if(image_type === 1){
      return Document
    }
    if(image_type === 3){
      return clinicaltrial
    }
    
    return Document
    
    
  }

  useEffect(() => {
    fetchData();
  }, []); // Run only once when the component mounts to fetch initial data

  useEffect(() => {
    // Check if timelineData has data before proceeding
    if (timelineData.length === 0) return;

    const datasetItems = new DataSet([]);
    timelineData.map(event => {
      const this_event = {id: event.Id, group: event.group, content: `<img src='${imageSelection(event.group)}' style='width: 28px; height: 28px;'> <a href=${event.hyperlink} target="_blank">${event.content}</a> `, editable: event.editable, type: event.type, className: event.className, start: event.start, end: event.end || event.start, title: event.title};
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
      editable:true,
      tooltip: {
				followMouse: true,
				template: function (originalItemData, parsedItemData) {
				//console.log(originalItemData)
				return `<div style="max-width:300px; word-wrap:break-word;">
							<p>${originalItemData.content}</p>${(originalItemData.title == null) ? '': `<p id="para1">${originalItemData.title} </p>`   }
						</div>
				`;
				//return ReactDOM.render(<b>{originalItemData.content}</b>, parsedItemData);
				},

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
    </>
  );
};