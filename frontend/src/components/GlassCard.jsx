import React from 'react';

const GlassCard = ({ children, className = '', glow = false, hoverGlow = true, title = '', headerAction = null }) => {
  return (
    <div className={`
      relative overflow-hidden rounded-xl border border-cyber-border/30 bg-cyber-card/75 backdrop-blur-cyber p-6 transition-all duration-300
      ${glow ? 'shadow-neon-accent border-cyber-accent/30' : 'shadow-glass'}
      ${hoverGlow ? 'hover:border-cyber-accent/40 hover:shadow-neon-accent' : ''}
      ${className}
    `}>
      {/* Accent Top Border Line */}
      <div className="absolute top-0 left-0 right-0 h-[2px] bg-gradient-to-r from-transparent via-cyber-accent/60 to-transparent" />
      
      {/* Background Mesh Flare */}
      <div className="absolute -right-20 -top-20 w-40 h-40 rounded-full bg-cyber-accent/5 blur-[80px] pointer-events-none" />

      {title && (
        <div className="flex justify-between items-center mb-4 pb-3 border-b border-cyber-border/10">
          <h3 className="text-lg font-cyber tracking-wider font-semibold text-cyber-accent text-glow-accent">
            &gt; {title}
          </h3>
          {headerAction}
        </div>
      )}
      
      <div className="relative z-10">
        {children}
      </div>
    </div>
  );
};

export default GlassCard;
