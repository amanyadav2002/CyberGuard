import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Dashboard from './pages/Dashboard';
import URLScanner from './pages/URLScanner';
import APKScanner from './pages/APKScanner';
import ModelComparison from './pages/ModelComparison';
import Login from './pages/Login';
import Register from './pages/Register';

const ProtectedRoute = ({ children }) => {
  const { token, loading } = useAuth();

  if (loading) {
    return (
      <div className="flex h-screen flex-col items-center justify-center bg-cyber-bg text-gray-500 font-cyber text-sm">
        <div className="h-10 w-10 animate-spin rounded-full border-2 border-t-transparent border-cyber-accent mb-4" />
        <span>INITIALIZING_SECURE_SHELL...</span>
      </div>
    );
  }

  if (!token) {
    return <Navigate to="/login" replace />;
  }

  return children;
};

function AppContent() {
  return (
    <div className="flex flex-col min-h-screen relative z-10 bg-cyber-bg/95">
      {/* Background Cyber Grid */}
      <div className="cyber-grid" />
      
      {/* Top Navbar */}
      <Navbar />
      
      {/* Main Contents */}
      <main className="flex-grow">
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/" element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          } />
          <Route path="/scan-url" element={
            <ProtectedRoute>
              <URLScanner />
            </ProtectedRoute>
          } />
          <Route path="/scan-apk" element={
            <ProtectedRoute>
              <APKScanner />
            </ProtectedRoute>
          } />
          <Route path="/models" element={
            <ProtectedRoute>
              <ModelComparison />
            </ProtectedRoute>
          } />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
      
      {/* Shared Footer */}
      <Footer />
    </div>
  );
}

function App() {
  return (
    <AuthProvider>
      <Router>
        <AppContent />
      </Router>
    </AuthProvider>
  );
}

export default App;
