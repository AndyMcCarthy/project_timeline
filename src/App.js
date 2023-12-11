import './App.css';
import {VisTimeline} from'./components/timeline'

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
      </header>


    </div>
  );
}

export default App;
