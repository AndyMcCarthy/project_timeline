import React from "react";

export const modalForm = () =>{

    return <>
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
    </>
}