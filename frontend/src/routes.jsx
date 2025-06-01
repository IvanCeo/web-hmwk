import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import AddForm from './components/AddForm';

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        {/* <Route path="/" element={<Home />} />
        <Route path="/product/list" element={} />
        <Route path="/product/:id" element={} />
        <Route path="/add" element={<AddForm />} /> */}
      </Routes>
    </Router>
  );
};

export default AppRoutes;