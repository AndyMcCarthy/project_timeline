import React, { useEffect, useRef, useState} from "react";
import {DataSet} from "vis-data";
import { Timeline } from "vis-timeline/standalone";
import Document from "./Document.png"
import './timeline.css'

export const VisTimeline = () => {
  const [timelineData, setTimelineData] = useState([]);

  const fetchData = async () => {
    try {
      const response = await fetch("http://localhost:8080/api/timeline");
      const data = await response.json();
      setTimelineData(data);
    } catch (error) {
      console.error("Error fetching timeline data:", error);
    }
  };

  const visJsContainer = useRef(null);

  useEffect(() => {
    fetchData();
  }, []); // Run only once when the component mounts to fetch initial data

  useEffect(() => {
    // Check if timelineData has data before proceeding
    if (timelineData.length === 0) return;

    const datasetItems = new DataSet([]);
    timelineData.map(event => {
      const this_event = {id: event.Id, group: event.group, content: event.content, editable: event.editable, type: event.type, className: event.className, start: event.start, end: event.start, title: event.title};
      datasetItems.add(this_event);
    });

    const groups = new DataSet([
      { id: 1, content: "Patents" },
      { id: 2, content: "Papers" },
    ]);

    const today = new Date();
    const options = {
      width: '100%',
      start: '2014-01-01',
      end: new Date().setFullYear(today.getFullYear() + 1)
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