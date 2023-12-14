import React, { useEffect, useRef} from "react";
import {DataSet} from "vis-data";
import { Timeline } from "vis-timeline/standalone";
import Document from "./Document.png"
import './timeline.css'

export const VisTimeline = () => {

    const visJsContainer = useRef(null);


      useEffect(() => {
         // Create a DataSet (allows two way data-binding)
         var groups = new DataSet([
            { id: 1, content: "Patents" },
            { id: 2, content: "Papers" },		
        ]);
        const today = new Date()
        var options = {
            width: '100%',
            start: '2014-01-01', // lower limit of visible range
            end: new Date().setFullYear(today.getFullYear() + 1) // upper limit 
        }
        

        // Create a DataSet (allows two way data-binding)
        var datasetItems= new DataSet([
            { id: `item1`, group:1, content: `<img src='${Document}' style='width: 28px; height: 28px;'> <a href="https://patentimages.storage.googleapis.com/55/df/ca/09af3f5d4ce33d/US8809292.pdf" target="_blank">PCSK9</a> `, editable: false, type:'box', className: "Patent", start: '2014-08-19', title: "siRNA PCSK9"},
            { id: `item2`, group:1, content: `<img src='${Document}' style='width: 28px; height: 28px;'> <a href="https://patentimages.storage.googleapis.com/28/40/cd/b42ef8e3a84681/WO2023192977A2.pdf" target="_blank">SNCA</a> `, editable: false, type:'box', className: "Patent", start: '2023-10-05', title: "siRNA SNCA"},
            { id: `item3`, group:1, content: `<img src='${Document}' style='width: 28px; height: 28px;'> <a href="https://patentimages.storage.googleapis.com/25/2f/00/6e133bb7be71e1/WO2023076450A2.pdf" target="_blank">HTT</a> `, editable: false, type:'box', className: "Patent", start: '2023-05-04', title: "siRNA HTT"},
            { id: `item4`, group:1, content: `<img src='${Document}' style='width: 28px; height: 28px;'> <a href="https://patentimages.storage.googleapis.com/28/b5/4b/1b0a9a9c0d0295/AU2023248138A1.pdf" target="_blank">TTR</a> `, editable: false, type:'box', className: "Patent", start: '2023-10-12', title: "siRNA TTR"},
            { id: `item5`, group:1, content: `<img src='${Document}' style='width: 28px; height: 28px;'> <a href="https://patentimages.storage.googleapis.com/68/26/0a/c060ee00f0d055/WO2023056478A1.pdf" target="_blank">ANGPTL7</a> `, editable: false, type:'box', className: "Patent", start: '2022-09-30', title: "siRNA ANGPTL7"},
            
            { id: `item6`, group:2, content: `<img src='${Document}' style='width: 28px; height: 28px;'> <a href="" target="_blank">Alnylam Patent 1</a> `, editable: false, type:'range', className: "External", start: '2021-06-16', end: '2022-06-29', title: "hello alynylam"},
            ]);

        const timeline = visJsContainer.current && new Timeline(visJsContainer.current, datasetItems, groups, options)

   
    },[visJsContainer])

return(
    <div>
      <div ref={visJsContainer} />
    </div>
)
}