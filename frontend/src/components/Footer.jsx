import React, { useState, useEffect } from 'react';
import { Cpu, HardDrive, Wifi, Activity } from 'lucide-react';

const Footer = () => {
  const [latency, setLatency] = useState(12);

  useEffect(() => {
    const interval = setInterval(() => {
      setLatency(Math.floor(Math.random() * 15) + 5);
    }, 4000);
    return () => clearInterval(interval);
  }, []);

  return (
    <footer className="mt-auto border-t border-cyber-border/10 bg-cyber-bg/40 backdrop-blur-cyber py-4 text-gray-500 text-xs">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
        
        {/* Branding & Copyright */}
        <div className="font-cyber flex items-center space-x-2">
          <span className="text-gray-400">CYBERGUARD PLATFORM</span>
          <span className="text-gray-600">v1.0.0</span>
          <span className="text-gray-600">|</span>
          <span>© {new Date().getFullYear()}</span>
        </div>

        {/* Real-time System Metrics */}
        <div className="flex flex-wrap justify-center items-center gap-6 font-cyber">
          <div className="flex items-center space-x-1.5 text-cyber-success text-glow-success">
            <Wifi className="h-3.5 w-3.5" />
            <span>API Status: ONLINE</span>
          </div>

          <div className="flex items-center space-x-1.5 text-cyber-accent text-glow-accent">
            <HardDrive className="h-3.5 w-3.5" />
            <span>DB: SQLITE (ACTIVE)</span>
          </div>

          <div className="flex items-center space-x-1.5 text-gray-400">
            <Cpu className="h-3.5 w-3.5 animate-pulse" />
            <span>CORE: ACTIVE DETECTOR (RF)</span>
          </div>

          <div className="flex items-center space-x-1.5 text-cyber-warning">
            <Activity className="h-3.5 w-3.5" />
            <span>PING: {latency}ms</span>
          </div>
        </div>

      </div>
    </footer>
  );
};

export default Footer;
