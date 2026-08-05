import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import GlassCard from '../components/GlassCard';
import { KeyRound, User, Eye, EyeOff, AlertTriangle, ShieldCheck } from 'lucide-react';

const Login = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const res = await login(username, password);
      if (res.success) {
        navigate('/');
      }
    } catch (err) {
      setError(err.message || 'Invalid credentials or connection error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex min-h-[calc(100vh-10rem)] items-center justify-center px-4 py-12 sm:px-6 lg:px-8 relative">
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-72 h-72 rounded-full bg-cyber-accent/5 blur-[120px] pointer-events-none" />

      <div className="w-full max-w-md space-y-8">
        <div className="text-center">
          <div className="inline-flex h-12 w-12 items-center justify-center rounded-full bg-cyber-accent/10 border border-cyber-accent/30 text-cyber-accent drop-shadow-[0_0_8px_rgba(0,240,255,0.3)] mb-4">
            <ShieldCheck className="h-6 w-6" />
          </div>
          <h2 className="text-3xl font-bold tracking-tight text-white font-cyber text-glow-accent">
            ACCESS_DENIED
          </h2>
          <p className="mt-2 text-sm text-gray-400">
            Please decrypt session parameters below to authenticate.
          </p>
        </div>

        <GlassCard className="mt-4" glow={true} hoverGlow={false}>
          <form className="space-y-6" onSubmit={handleSubmit}>
            {error && (
              <div className="flex items-center space-x-2 text-xs border border-cyber-danger/30 bg-cyber-danger-dim text-cyber-danger p-3 rounded">
                <AlertTriangle className="h-4 w-4 shrink-0" />
                <span className="font-cyber">{error}</span>
              </div>
            )}

            <div>
              <label htmlFor="username" className="block text-xs font-cyber text-gray-400 uppercase tracking-wider mb-2">
                &gt; USERNAME
              </label>
              <div className="relative">
                <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3 text-gray-500">
                  <User className="h-4 w-4" />
                </div>
                <input
                  id="username"
                  name="username"
                  type="text"
                  required
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="block w-full rounded-md border border-cyber-border/40 bg-black/40 py-2.5 pl-10 pr-3 text-sm text-gray-100 placeholder-gray-500 focus:border-cyber-accent focus:outline-none focus:ring-1 focus:ring-cyber-accent font-cyber"
                  placeholder="admin"
                />
              </div>
            </div>

            <div>
              <label htmlFor="password" className="block text-xs font-cyber text-gray-400 uppercase tracking-wider mb-2">
                &gt; DECRYPTION_KEY
              </label>
              <div className="relative">
                <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3 text-gray-500">
                  <KeyRound className="h-4 w-4" />
                </div>
                <input
                  id="password"
                  name="password"
                  type={showPassword ? 'text' : 'password'}
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="block w-full rounded-md border border-cyber-border/40 bg-black/40 py-2.5 pl-10 pr-10 text-sm text-gray-100 placeholder-gray-500 focus:border-cyber-accent focus:outline-none focus:ring-1 focus:ring-cyber-accent font-cyber"
                  placeholder="••••••••"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-500 hover:text-gray-300"
                >
                  {showPassword ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                </button>
              </div>
            </div>

            <div>
              <button
                type="submit"
                disabled={loading}
                className="group relative flex w-full justify-center rounded-md border border-cyber-accent bg-cyber-accent-dim py-2.5 text-sm font-medium text-cyber-accent hover:bg-cyber-accent hover:text-cyber-bg hover:shadow-neon-accent-strong focus:outline-none transition-all duration-300 font-cyber tracking-widest disabled:opacity-50"
              >
                {loading ? 'AUTHENTICATING...' : 'AUTHORIZE_ACCESS'}
              </button>
            </div>
          </form>

          <div className="mt-6 text-center text-xs">
            <span className="text-gray-500 font-cyber">NEW_AGENT?</span>{' '}
            <Link to="/register" className="font-cyber font-bold text-cyber-accent hover:text-cyan-400 underline transition-colors">
              REGISTER_CREDENTIALS
            </Link>
          </div>
        </GlassCard>
      </div>
    </div>
  );
};

export default Login;
