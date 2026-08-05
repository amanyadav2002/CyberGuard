import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import GlassCard from '../components/GlassCard';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from 'recharts';
import { Shield, ShieldAlert, ShieldCheck, Brain, Clock, Trash2, Search, ArrowUpRight, ShieldQuestion } from 'lucide-react';
import { Link } from 'react-router-dom';

const Dashboard = () => {
  const { token } = useAuth();
  const [metrics, setMetrics] = useState({
    totalScans: 0,
    maliciousCount: 0,
    safeCount: 0,
    ratio: 0,
    activeModel: 'Random Forest'
  });
  const [scans, setScans] = useState([]);
  const [search, setSearch] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDashboardData();
  }, [token]);

  const fetchDashboardData = async () => {
    setLoading(true);
    try {
      const reportRes = await fetch('http://localhost:8000/api/reports/dashboard', {
        headers: token ? { 'Authorization': `Bearer ${token}` } : {}
      });
      const activeModelRes = await fetch('http://localhost:8000/api/models/active');
      
      let dashboardData = null;
      let activeModel = 'Random Forest';

      if (reportRes.ok) {
        dashboardData = await reportRes.json();
      }
      if (activeModelRes.ok) {
        const modelInfo = await activeModelRes.json();
        activeModel = modelInfo.active_model;
      }

      if (dashboardData) {
        setMetrics({
          totalScans: dashboardData.total_scans,
          maliciousCount: dashboardData.malicious_scans,
          safeCount: dashboardData.safe_scans,
          ratio: dashboardData.threat_ratio,
          activeModel
        });
        setScans(dashboardData.scans || []);
      } else {
        throw new Error("No backend response");
      }
    } catch (error) {
      console.warn("Backend offline, utilizing fallback state for Dashboard");
      loadLocalMockData();
    } finally {
      setLoading(false);
    }
  };

  const loadLocalMockData = () => {
    const storedScans = localStorage.getItem('cg_scans');
    let scanList = [];
    if (storedScans) {
      scanList = JSON.parse(storedScans);
    } else {
      scanList = [
        { id: 1, type: 'URL', target: 'http://secure-bank-login-verify.com/login', score: 94.2, result: 'Malicious', timestamp: '2026-08-05T20:10:00Z', active_model: 'Random Forest', metadata: { ip_host: true, dot_count: 3, sensitive_words: true } },
        { id: 2, type: 'APK', target: 'root-exploit-payload.apk', score: 88.5, result: 'Malicious', timestamp: '2026-08-05T19:40:00Z', active_model: 'Random Forest', metadata: { permissions_count: 24, requested_boot_receiver: true, target_sdk: 29 } },
        { id: 3, type: 'URL', target: 'https://github.com/google/deepmind', score: 2.1, result: 'Safe', timestamp: '2026-08-05T18:15:00Z', active_model: 'Support Vector Machine', metadata: { ip_host: false, dot_count: 1, sensitive_words: false } },
        { id: 4, type: 'APK', target: 'clean-flashlight-utility.apk', score: 14.3, result: 'Safe', timestamp: '2026-08-05T14:30:00Z', active_model: 'Random Forest', metadata: { permissions_count: 3, requested_boot_receiver: false, target_sdk: 33 } }
      ];
      localStorage.setItem('cg_scans', JSON.stringify(scanList));
    }

    const total = scanList.length;
    const malicious = scanList.filter(s => s.result === 'Malicious' || s.score >= 50).length;
    const safe = total - malicious;
    const activeModel = localStorage.getItem('cg_active_model') || 'Random Forest';

    setScans(scanList);
    setMetrics({
      totalScans: total,
      maliciousCount: malicious,
      safeCount: safe,
      ratio: total > 0 ? parseFloat(((malicious / total) * 100).toFixed(1)) : 0,
      activeModel
    });
  };

  const clearHistory = async () => {
    if (!window.confirm("Are you sure you want to purge the threat logs database?")) return;
    try {
      const response = await fetch('http://localhost:8000/api/reports/clear', {
        method: 'DELETE',
        headers: token ? { 'Authorization': `Bearer ${token}` } : {}
      });
      if (response.ok) {
        fetchDashboardData();
      } else {
        throw new Error("Clear request rejected");
      }
    } catch (err) {
      console.warn("Backend offline, purging localStorage");
      localStorage.removeItem('cg_scans');
      loadLocalMockData();
    }
  };

  const filteredScans = scans
    .filter(scan => scan.target.toLowerCase().includes(search.toLowerCase()))
    .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

  const chartData = [
    { name: 'Malicious Scans', value: metrics.maliciousCount, color: '#ff0055' },
    { name: 'Safe Scans', value: metrics.safeCount, color: '#00ff66' }
  ];

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8 space-y-8 relative">
      <div className="absolute top-0 right-1/4 w-96 h-96 rounded-full bg-cyber-accent/5 blur-[120px] pointer-events-none" />

      {/* Header */}
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center space-y-4 sm:space-y-0">
        <div>
          <h1 className="text-3xl font-bold tracking-tight text-white font-cyber text-glow-accent">
            SECURITY_DASHBOARD
          </h1>
          <p className="text-sm text-gray-400">
            Real-time phishing detection heuristics & static binary analyzers.
          </p>
        </div>
        <button 
          onClick={fetchDashboardData}
          className="px-4 py-2 border border-cyber-accent bg-cyber-accent-dim hover:bg-cyber-accent hover:text-cyber-bg transition-all duration-300 rounded font-cyber text-xs uppercase tracking-widest text-cyber-accent"
        >
          SYNC_METRICS
        </button>
      </div>

      {/* Metrics Row */}
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <GlassCard title="TOTAL_SCANS" hoverGlow={true}>
          <div className="flex items-baseline space-x-2">
            <span className="text-4xl font-bold font-cyber text-white">
              {metrics.totalScans}
            </span>
            <span className="text-xs text-gray-500 font-cyber">SCANS</span>
          </div>
          <p className="mt-2 text-xs text-gray-400">Aggregate check log counter</p>
        </GlassCard>

        <GlassCard title="MALICIOUS_RATIO" hoverGlow={true}>
          <div className="flex items-baseline space-x-2">
            <span className={`text-4xl font-bold font-cyber ${metrics.ratio > 40 ? 'text-cyber-danger text-glow-danger' : 'text-cyber-warning'}`}>
              {metrics.ratio}%
            </span>
          </div>
          <p className="mt-2 text-xs text-gray-400">Threat ratio density coefficient</p>
        </GlassCard>

        <GlassCard title="THREAT_COUNT" hoverGlow={true}>
          <div className="flex items-baseline space-x-2">
            <span className="text-4xl font-bold font-cyber text-cyber-danger text-glow-danger">
              {metrics.maliciousCount}
            </span>
            <span className="text-xs text-gray-500 font-cyber">MALICIOUS</span>
          </div>
          <p className="mt-2 text-xs text-gray-400">Confirmed cyber threat targets</p>
        </GlassCard>

        <GlassCard title="ACTIVE_DETECTOR" hoverGlow={true}>
          <div className="flex items-baseline space-x-2">
            <span className="text-xl font-bold font-cyber text-cyber-accent text-glow-accent truncate max-w-full">
              {metrics.activeModel}
            </span>
          </div>
          <p className="mt-2 text-xs text-gray-400">Active machine learning backend</p>
        </GlassCard>
      </div>

      {/* Charts & Threat distribution */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <GlassCard title="THREAT_DISTRIBUTION" className="lg:col-span-1 flex flex-col justify-between">
          {metrics.totalScans > 0 ? (
            <div className="h-64 relative flex flex-col justify-center items-center">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={chartData.filter(d => d.value > 0)}
                    cx="50%"
                    cy="50%"
                    innerRadius={60}
                    outerRadius={80}
                    paddingAngle={5}
                    dataKey="value"
                  >
                    {chartData.filter(d => d.value > 0).map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip 
                    contentStyle={{ backgroundColor: 'rgba(8, 9, 10, 0.95)', borderColor: 'rgba(0, 240, 255, 0.2)', color: '#fff' }}
                    itemStyle={{ color: '#fff' }}
                  />
                </PieChart>
              </ResponsiveContainer>
              <div className="absolute flex flex-col items-center justify-center">
                <span className="text-xs text-gray-500 font-cyber">RATIO</span>
                <span className="text-2xl font-bold font-cyber text-white">{metrics.ratio}%</span>
              </div>
            </div>
          ) : (
            <div className="h-64 flex flex-col items-center justify-center text-gray-500">
              <ShieldQuestion className="h-12 w-12 mb-2 animate-pulse text-gray-600" />
              <span className="text-xs font-cyber">NO_THREATS_FOUND</span>
            </div>
          )}

          <div className="space-y-2 mt-4">
            <div className="flex justify-between items-center text-xs">
              <div className="flex items-center space-x-2">
                <div className="w-2.5 h-2.5 rounded-full bg-cyber-danger" />
                <span className="text-gray-400 font-cyber">Malicious Scans</span>
              </div>
              <span className="font-cyber font-bold text-white">{metrics.maliciousCount}</span>
            </div>
            <div className="flex justify-between items-center text-xs">
              <div className="flex items-center space-x-2">
                <div className="w-2.5 h-2.5 rounded-full bg-cyber-success" />
                <span className="text-gray-400 font-cyber">Safe Scans</span>
              </div>
              <span className="font-cyber font-bold text-white">{metrics.safeCount}</span>
            </div>
          </div>
        </GlassCard>

        {/* Quick Launch scan vectors */}
        <GlassCard title="SCAN_VECTORS" className="lg:col-span-2 flex flex-col justify-between">
          <div className="space-y-4">
            <p className="text-sm text-gray-400">
              Launch static extraction pipelines and score binaries or link structures:
            </p>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <Link 
                to="/scan-url"
                className="group relative overflow-hidden flex flex-col justify-between p-5 rounded-lg border border-cyber-border/30 bg-black/40 hover:border-cyber-accent hover:shadow-neon-accent transition-all duration-300"
              >
                <div className="flex justify-between items-start">
                  <ShieldCheck className="h-8 w-8 text-cyber-accent group-hover:scale-110 transition-transform duration-300" />
                  <ArrowUpRight className="h-4 w-4 text-gray-500 group-hover:text-cyber-accent group-hover:translate-x-1 group-hover:-translate-y-1 transition-all duration-300" />
                </div>
                <div className="mt-8">
                  <h4 className="font-cyber font-bold text-white group-hover:text-cyber-accent transition-colors">URL_SCANNER</h4>
                  <p className="text-xs text-gray-500 mt-1">Lexical analysis and domain structural threat profiling</p>
                </div>
              </Link>

              <Link 
                to="/scan-apk"
                className="group relative overflow-hidden flex flex-col justify-between p-5 rounded-lg border border-cyber-border/30 bg-black/40 hover:border-cyber-accent hover:shadow-neon-accent transition-all duration-300"
              >
                <div className="flex justify-between items-start">
                  <ShieldAlert className="h-8 w-8 text-cyber-danger group-hover:scale-110 transition-transform duration-300" />
                  <ArrowUpRight className="h-4 w-4 text-gray-500 group-hover:text-cyber-danger group-hover:translate-x-1 group-hover:-translate-y-1 transition-all duration-300" />
                </div>
                <div className="mt-8">
                  <h4 className="font-cyber font-bold text-white group-hover:text-cyber-danger transition-colors">APK_SCANNER</h4>
                  <p className="text-xs text-gray-500 mt-1">Decompiles Android packages, inspects permissions and services</p>
                </div>
              </Link>
            </div>
          </div>

          <div className="mt-6 border-t border-cyber-border/10 pt-4 flex justify-between items-center text-xs text-gray-500 font-cyber">
            <span>READY_FOR_INCOMING_DATALINKS</span>
            <span className="flex items-center space-x-1">
              <span className="w-1.5 h-1.5 rounded-full bg-cyber-success animate-ping" />
              <span className="text-cyber-success">DAEMON: RUNNING</span>
            </span>
          </div>
        </GlassCard>
      </div>

      {/* History Log Feed */}
      <GlassCard 
        title="THREAT_LOGS_FEED"
        headerAction={
          scans.length > 0 && (
            <button
              onClick={clearHistory}
              className="flex items-center space-x-1 text-xs font-cyber text-cyber-danger hover:underline"
            >
              <Trash2 className="h-3.5 w-3.5" />
              <span>PURGE_DATABASE</span>
            </button>
          )
        }
      >
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-4">
          <div className="relative w-full sm:max-w-xs">
            <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3 text-gray-500">
              <Search className="h-4 w-4" />
            </div>
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Filter by target..."
              className="block w-full rounded-md border border-cyber-border/20 bg-black/40 py-1.5 pl-10 pr-3 text-xs text-gray-300 placeholder-gray-600 focus:border-cyber-accent focus:outline-none font-cyber"
            />
          </div>
          <span className="text-xs text-gray-500 font-cyber">
            MATCHING_LOGS: {filteredScans.length}
          </span>
        </div>

        {loading ? (
          <div className="flex h-32 flex-col items-center justify-center text-gray-500">
            <div className="h-8 w-8 animate-spin rounded-full border-2 border-t-transparent border-cyber-accent mb-2" />
            <span className="text-xs font-cyber">DECRYPTING_DATALOGS...</span>
          </div>
        ) : filteredScans.length > 0 ? (
          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="border-b border-cyber-border/10 font-cyber text-xs text-gray-500 tracking-wider">
                  <th className="py-3 px-4">VECTOR</th>
                  <th className="py-3 px-4">TARGET_SPECIFIER</th>
                  <th className="py-3 px-4">RISK_INDEX</th>
                  <th className="py-3 px-4">ML_CLASSIFIER</th>
                  <th className="py-3 px-4">TIMESTAMP</th>
                  <th className="py-3 px-4">STATUS</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-cyber-border/5 text-xs font-cyber">
                {filteredScans.map((scan) => {
                  const isHighRisk = scan.score >= 50;
                  return (
                    <tr key={scan.id} className="hover:bg-white/5 transition-colors">
                      <td className="py-3 px-4">
                        <span className={`inline-block px-2 py-0.5 rounded text-[10px] uppercase font-bold ${
                          scan.type === 'URL' ? 'bg-cyber-accent-dim text-cyber-accent border border-cyber-accent/20' : 'bg-fuchsia-950 text-fuchsia-400 border border-fuchsia-800/30'
                        }`}>
                          {scan.type}
                        </span>
                      </td>
                      <td className="py-3 px-4 font-mono max-w-xs truncate text-gray-300">
                        {scan.target}
                      </td>
                      <td className="py-3 px-4">
                        <span className={`font-bold ${isHighRisk ? 'text-cyber-danger' : 'text-cyber-success'}`}>
                          {scan.score.toFixed(1)}%
                        </span>
                      </td>
                      <td className="py-3 px-4 text-gray-500">
                        {scan.active_model}
                      </td>
                      <td className="py-3 px-4 text-gray-500">
                        {new Date(scan.timestamp).toLocaleString()}
                      </td>
                      <td className="py-3 px-4">
                        <div className="flex items-center space-x-1">
                          {isHighRisk ? (
                            <>
                              <ShieldAlert className="h-3.5 w-3.5 text-cyber-danger animate-pulse" />
                              <span className="text-cyber-danger">THREAT_DETECTED</span>
                            </>
                          ) : (
                            <>
                              <ShieldCheck className="h-3.5 w-3.5 text-cyber-success" />
                              <span className="text-cyber-success">SECURED</span>
                            </>
                          )}
                        </div>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="flex h-32 flex-col items-center justify-center border border-dashed border-cyber-border/20 rounded-lg text-gray-500">
            <Clock className="h-8 w-8 mb-2 text-gray-600" />
            <span className="text-xs font-cyber">NO_THREAT_RECORDS_AVAILABLE</span>
          </div>
        )}
      </GlassCard>
    </div>
  );
};

export default Dashboard;
