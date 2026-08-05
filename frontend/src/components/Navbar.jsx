import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { Shield, LayoutDashboard, Link2, FileCode, BarChart3, LogOut, LogIn, Menu, X, Terminal } from 'lucide-react';

const Navbar = () => {
  const { user, logout } = useAuth();
  const location = useLocation();
  const [isOpen, setIsOpen] = useState(false);

  const navItems = [
    { name: 'Dashboard', path: '/', icon: LayoutDashboard },
    { name: 'URL Scanner', path: '/scan-url', icon: Link2 },
    { name: 'APK Scanner', path: '/scan-apk', icon: FileCode },
    { name: 'Model Comparison', path: '/models', icon: BarChart3 },
  ];

  const isActive = (path) => location.pathname === path;

  return (
    <nav className="sticky top-0 z-50 w-full border-b border-cyber-border/20 bg-cyber-bg/75 backdrop-blur-cyber">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-2 group">
            <Shield className="h-8 w-8 text-cyber-accent group-hover:scale-110 transition-transform duration-300 drop-shadow-[0_0_8px_rgba(0,240,255,0.5)]" />
            <span className="font-cyber text-xl font-bold tracking-widest text-transparent bg-clip-text bg-gradient-to-r from-cyber-accent to-white group-hover:text-glow-accent transition-all duration-300">
              CYBER<span className="text-cyber-accent">GUARD</span>
            </span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-1 lg:space-x-4">
            {navItems.map((item) => {
              const Icon = item.icon;
              const active = isActive(item.path);
              return (
                <Link
                  key={item.name}
                  to={item.path}
                  className={`flex items-center space-x-2 px-3 py-2 rounded-md font-cyber text-sm tracking-wider transition-all duration-300 ${
                    active 
                      ? 'text-cyber-accent bg-cyber-accent-dim border border-cyber-accent/30 shadow-neon-accent' 
                      : 'text-gray-400 hover:text-white hover:bg-white/5 border border-transparent'
                  }`}
                >
                  <Icon className="h-4 w-4" />
                  <span>{item.name}</span>
                </Link>
              );
            })}
          </div>

          {/* Auth section */}
          <div className="hidden md:flex items-center space-x-4">
            {user ? (
              <div className="flex items-center space-x-4">
                <div className="flex items-center space-x-2 px-3 py-1 rounded bg-black/40 border border-cyber-border/10">
                  <Terminal className="h-3.5 w-3.5 text-cyber-accent animate-pulse" />
                  <span className="font-cyber text-xs text-gray-300 tracking-wider">
                    {user.username}
                  </span>
                </div>
                <button
                  onClick={logout}
                  className="flex items-center space-x-2 px-3 py-2 rounded-md font-cyber text-sm tracking-wider text-cyber-danger hover:bg-cyber-danger-dim border border-transparent hover:border-cyber-danger/30 transition-all duration-300"
                >
                  <LogOut className="h-4 w-4" />
                  <span>Logout</span>
                </button>
              </div>
            ) : (
              <div className="flex items-center space-x-2">
                <Link
                  to="/login"
                  className="flex items-center space-x-2 px-3 py-2 rounded-md font-cyber text-sm tracking-wider text-gray-400 hover:text-white hover:bg-white/5 transition-all duration-300"
                >
                  <LogIn className="h-4 w-4" />
                  <span>Login</span>
                </Link>
                <Link
                  to="/register"
                  className="flex items-center space-x-2 px-3.5 py-2 rounded-md font-cyber text-sm tracking-wider text-cyber-bg bg-cyber-accent font-bold hover:shadow-neon-accent-strong hover:bg-cyan-400 transition-all duration-300"
                >
                  <span>Sign Up</span>
                </Link>
              </div>
            )}
          </div>

          {/* Mobile menu button */}
          <div className="flex md:hidden">
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-white/5 focus:outline-none"
            >
              {isOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="md:hidden border-t border-cyber-border/10 bg-cyber-bg/95 backdrop-blur-md px-2 pt-2 pb-4 space-y-1">
          {navItems.map((item) => {
            const Icon = item.icon;
            const active = isActive(item.path);
            return (
              <Link
                key={item.name}
                to={item.path}
                onClick={() => setIsOpen(false)}
                className={`flex items-center space-x-3 px-3 py-2.5 rounded-md font-cyber text-base tracking-wider transition-all ${
                  active 
                    ? 'text-cyber-accent bg-cyber-accent-dim border border-cyber-accent/20' 
                    : 'text-gray-400 hover:text-white hover:bg-white/5'
                }`}
              >
                <Icon className="h-5 w-5" />
                <span>{item.name}</span>
              </Link>
            );
          })}
          <div className="pt-4 pb-2 border-t border-cyber-border/10">
            {user ? (
              <div className="px-3 space-y-3">
                <div className="flex items-center space-x-2">
                  <Terminal className="h-4 w-4 text-cyber-accent" />
                  <span className="font-cyber text-sm text-gray-300">{user.username}</span>
                </div>
                <button
                  onClick={() => {
                    logout();
                    setIsOpen(false);
                  }}
                  className="flex w-full items-center space-x-3 py-2.5 text-cyber-danger font-cyber text-base"
                >
                  <LogOut className="h-5 w-5" />
                  <span>Logout</span>
                </button>
              </div>
            ) : (
              <div className="px-3 space-y-2">
                <Link
                  to="/login"
                  onClick={() => setIsOpen(false)}
                  className="flex items-center space-x-3 py-2.5 text-gray-400 hover:text-white font-cyber text-base"
                >
                  <LogIn className="h-5 w-5" />
                  <span>Login</span>
                </Link>
                <Link
                  to="/register"
                  onClick={() => setIsOpen(false)}
                  className="flex items-center justify-center py-2.5 text-cyber-bg bg-cyber-accent font-bold rounded-md font-cyber text-base"
                >
                  <span>Sign Up</span>
                </Link>
              </div>
            )}
          </div>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
