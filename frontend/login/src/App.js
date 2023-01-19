
import './App.css';
import Header from './components/common/Header';
import Footer from './components/common/Footer';
import List from './components/List';
import Signup from './components/Signup';

function App() {
  return (
    <div className="App">
      <Header />
      <hr/>
      <List />,
      <hr />
      <Signup />
      <hr />
      <Footer />
    </div>
  );
}

export default App;
