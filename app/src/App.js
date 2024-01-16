import './App.css';
import {VisTimeline} from'./components/timeline/timeline'
import {ChatToData} from'./components/chatToData/chatToData'

function App() {
  return (
    <div className="Timeline">
      <header className="Timeline-header">
        <p>
          Project Timeline with PaperQA!
        </p>
        <div>
       <VisTimeline></VisTimeline>
       </div>
       <div>
        <ChatToData></ChatToData>
       </div>
      </header>


    </div>
  );
}

export default App;
