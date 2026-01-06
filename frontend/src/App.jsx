import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import TreeExplorer from './pages/TreeExplorer'
import SpiralPage from './pages/SpiralPage'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />} />
          <Route path="tree" element={<TreeExplorer />} />
          <Route path="spiral" element={<SpiralPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
