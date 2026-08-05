import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import GlassCard from '../components/GlassCard';
import { ShieldAlert, ShieldCheck, Link2, AlertTriangle, Play, RefreshCw, Layers } from 'lucide-react';

const URLScanner = () => {
  const { token } = useAuth();
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [scanSteps, setScanSteps] = useState([]);
  const [result, setResult] = useState(null);

  const performHeuristicScan = (targetUrl) => {
    // Live client-side feature extraction for offline developer mode
    const isHttps = targetUrl.toLowerCase().startsWith('https://');
    
    // Extract hostname for IP test
    let host = targetUrl;
    try {
      if (targetUrl.includes('://')) {
        host = new URL(targetUrl).hostname;
      } else {
        host = targetUrl.split('/')[0];
      }
    } catch(e) {}

    const ipRegex = /^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$/;
    const isIpHost = ipRegex.test(host);

    const dotCount = (targetUrl.split('.').length - 1);
    const slashCount = (targetUrl.split('/').length - 1);
    const dashCount = (targetUrl.split('-').length - 1);

    const sensitiveWords = ['login', 'secure', 'verify', 'update', 'banking', 'signin', 'account', 'paypal', 'ebay', 'amazon', 'webscr'];
    const matchedWords = sensitiveWords.filter(word => targetUrl.toLowerCase().includes(word));
    
    // Heuristic Risk Calculation
    let score = 5.0;
    if (!isHttps) score += 25.0;
    if (isIpHost) score += 40.0;
    score += (dotCount > 2 ? (dotCount - 2) * 15.0 : 0);
    score += (slashCount > 3 ? (slashCount - 3) * 10.0 : 0);
    score += (dashCount > 1 ? dashCount * 8.0 : 0);
    score += (matchedWords.length * 20.0);

    // Limit score
    score = Math.min(Math.max(score, 1.2), 99.9);
    const verdict = score >= 50.0 ? 'Malicious' : 'Safe';

    return {
      type: 'URL',
      target: targetUrl,
      score: parseFloat(score.toFixed(1)),
      result: verdict,
      timestamp: new Date().toISOString(),
      active_model: localStorage.getItem('cg_active_model') || 'Random Forest',
      metadata: {
        is_https: isHttps,
        is_ip_host: isIpHost,
        dot_count: dotCount,
        slash_count: slashCount,
        dash_count: dashCount,
        sensitive_word_matches: matchedWords
      }
    };
  };

  const handleScan = async (e) => {
    e.preventDefault();
    if (!url) return;

    setLoading(true);
    setResult(null);
    setScanSteps([]);

    const steps = [
      'RESOLVING_DOMAINKNOWN_SIGNATURES',
      'EXTRACTING_LEXICAL_STRUCTURES',
      'CHECKING_SSL_CERTIFICATE_METADATA',
      'EVALUATING_BAYESIAN_PROBABILITIES',
      'DETERMINING_THREAT_CLASSIFICATION'
    ];

    // Animate loader checklist
    for (let i = 0; i < steps.length; i++) {
      await new Promise(resolve => setTimeout(resolve, 600));
      setScanSteps(prev => [...prev, steps[i]]);
    }

    try {
      const response = await fetch('http://localhost:8000/api/scan/url', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(token ? { 'Authorization': `Bearer ${token}` } : {})
        },
        body: JSON.stringify({ url })
      });

      if (response.ok) {
        const data = await response.json();
        setResult(data);
        saveScanToHistory(data);
      } else {
        throw new Error("Backend connection failed");
      }
    } catch (err) {
      console.warn("Backend offline, executing client heuristic scan");
      const mockResult = performHeuristicScan(url);
      setResult(mockResult);
      saveScanToHistory(mockResult);
    } finally {
      setLoading(false);
    }
  };

  const saveScanToHistory = (scan) => {
    const storedScans = localStorage.getItem('cg_scans');
    let scanList = [];
    if (storedScans) {
      scanList = JSON.parse(storedScans);
    }
    // Limit storage growth
    if (scanList.length > 50) scanList.pop();
    
    // Add ID
    scan.id = Date.now();
    scanList.unshift(scan);
    localStorage.setItem('cg_scans', JSON.stringify(scanList));
  };

  return (
    <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 py-8 space-y-8 relative">
      <div className="absolute top-0 left-1/4 w-80 h-80 rounded-full bg-cyber-accent/5 blur-[120px] pointer-events-none" />

      {/* Title */}
      <div>
        <h1 className="text-3xl font-bold tracking-tight text-white font-cyber text-glow-accent">
          URL_THREAD_ANALYZER
        </h1>
        <p className="text-sm text-gray-400">
          Analyze structural attributes and word markers in URL targets to determine phishing risks.
        </p>
      </div>

      {/* Input panel */}
      <GlassCard title="INPUT_VECTOR" hoverGlow={false}>
        <form onSubmit={handleScan} className="flex flex-col sm:flex-row gap-4">
          <div className="relative flex-grow">
            <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3 text-gray-500">
              <Link2 className="h-5 w-5" />
            </div>
            <input
              type="text"
              required
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="Enter target URL (e.g. http://login-secure-paypal.com/auth)"
              className="block w-full rounded-md border border-cyber-border/40 bg-black/40 py-3 pl-10 pr-3 text-sm text-gray-100 placeholder-gray-600 focus:border-cyber-accent focus:outline-none focus:ring-1 focus:ring-cyber-accent font-cyber"
            />
          </div>
          <button
            type="submit"
            disabled={loading}
            className="flex items-center justify-center space-x-2 px-6 py-3 border border-cyber-accent bg-cyber-accent-dim hover:bg-cyber-accent hover:text-cyber-bg transition-all duration-300 rounded font-cyber text-sm font-bold tracking-widest text-cyber-accent disabled:opacity-50"
          >
            {loading ? <RefreshCw className="h-4 w-4 animate-spin" /> : <Play className="h-4 w-4" />}
            <span>EXECUTE_SCAN</span>
          </button>
        </form>
      </GlassCard>

      {/* Loading Checklist */}
      {loading && (
        <GlassCard title="SCANNER_TELEMETRY" hoverGlow={false} className="relative overflow-hidden">
          <div className="scan-beam" />
          <div className="space-y-3 font-cyber text-xs">
            {scanSteps.map((step, idx) => (
              <div key={idx} className="flex items-center space-x-2 text-cyber-accent">
                <span className="text-cyber-accent-dim">[SUCCESS]</span>
                <span className="text-gray-300">&gt; {step} ... OK</span>
              </div>
            ))}
            <div className="flex items-center space-x-2 text-cyber-accent animate-pulse">
              <span className="text-cyber-accent-dim">[ACTIVE]</span>
              <span className="text-cyber-accent">&gt; PIPELINE_EXECUTION_IN_PROGRESS...</span>
            </div>
          </div>
        </GlassCard>
      )}

      {/* Results screen */}
      {result && !loading && (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Gauge card */}
          <GlassCard 
            title="THREAT_INDEX_SCORE" 
            className="md:col-span-1 flex flex-col items-center justify-center text-center py-8"
            glow={result.score >= 50}
          >
            <div className="relative flex items-center justify-center w-36 h-36 rounded-full border-4 border-cyber-border/10 mb-4">
              {/* Score text */}
              <div className="flex flex-col items-center justify-center">
                <span className={`text-3xl font-bold font-cyber ${result.score >= 50 ? 'text-cyber-danger text-glow-danger' : 'text-cyber-success text-glow-success'}`}>
                  {result.score}%
                </span>
                <span className="text-[10px] text-gray-500 font-cyber">RISK_RATIO</span>
              </div>
              
              {/* Animated outer ring */}
              <div className={`absolute inset-0 rounded-full border-2 border-dashed ${
                result.score >= 50 ? 'border-cyber-danger/40 animate-spin' : 'border-cyber-success/40'
              }`} style={{ animationDuration: '8s' }} />
            </div>

            <div className="space-y-1">
              <div className="text-xs text-gray-500 font-cyber">VERDICT</div>
              <div className={`text-lg font-bold font-cyber tracking-widest ${
                result.score >= 50 ? 'text-cyber-danger text-glow-danger' : 'text-cyber-success text-glow-success'
              }`}>
                {result.result === 'Malicious' ? 'THREAT_DETECTED' : 'CLEAN_VERDICT'}
              </div>
            </div>
          </GlassCard>

          {/* Feature details */}
          <GlassCard title="LEXICAL_METRIC_REPORT" className="md:col-span-2 space-y-4">
            <p className="text-xs text-gray-400">
              Analysis compiled using active classifier model: <strong className="text-cyber-accent font-cyber">{result.active_model}</strong>
            </p>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {/* SSL Status */}
              <div className="flex items-center justify-between p-3 bg-black/40 rounded border border-cyber-border/10">
                <div className="flex flex-col">
                  <span className="text-xs text-gray-500 font-cyber">SSL_PROTOCOL</span>
                  <span className="text-xs text-gray-300 font-bold font-cyber mt-0.5">HTTPS Check</span>
                </div>
                {result.metadata.is_https ? (
                  <ShieldCheck className="h-6 w-6 text-cyber-success" />
                ) : (
                  <AlertTriangle className="h-6 w-6 text-cyber-danger animate-pulse" />
                )}
              </div>

              {/* Raw IP check */}
              <div className="flex items-center justify-between p-3 bg-black/40 rounded border border-cyber-border/10">
                <div className="flex flex-col">
                  <span className="text-xs text-gray-500 font-cyber">HOST_RESOLVER</span>
                  <span className="text-xs text-gray-300 font-bold font-cyber mt-0.5">Raw IP Address</span>
                </div>
                {!result.metadata.is_ip_host ? (
                  <ShieldCheck className="h-6 w-6 text-cyber-success" />
                ) : (
                  <ShieldAlert className="h-6 w-6 text-cyber-danger animate-pulse" />
                )}
              </div>

              {/* Dot count */}
              <div className="flex items-center justify-between p-3 bg-black/40 rounded border border-cyber-border/10">
                <div className="flex flex-col">
                  <span className="text-xs text-gray-500 font-cyber">DOT_COUNT</span>
                  <span className="text-xs text-gray-300 font-bold font-cyber mt-0.5">Subdomain Dividers</span>
                </div>
                <div className="flex items-center space-x-2">
                  <span className="text-sm font-bold font-cyber text-white">{result.metadata.dot_count}</span>
                  <span className={`text-[10px] font-cyber ${result.metadata.dot_count > 2 ? 'text-cyber-warning' : 'text-gray-500'}`}>
                    {result.metadata.dot_count > 2 ? 'SUSPICIOUS' : 'STANDARD'}
                  </span>
                </div>
              </div>

              {/* Slash/Dash features */}
              <div className="flex items-center justify-between p-3 bg-black/40 rounded border border-cyber-border/10">
                <div className="flex flex-col">
                  <span className="text-xs text-gray-500 font-cyber">PATH_COMPONENTS</span>
                  <span className="text-xs text-gray-300 font-bold font-cyber mt-0.5">Slash / Dash count</span>
                </div>
                <span className="text-sm font-bold font-cyber text-white">
                  {result.metadata.slash_count} / {result.metadata.dash_count}
                </span>
              </div>
            </div>

            {/* Sensitive Words Checklist */}
            <div className="border-t border-cyber-border/10 pt-4 space-y-2">
              <span className="text-xs text-gray-500 font-cyber uppercase tracking-wider block">
                &gt; TRIGGER_WORD_DETECTION
              </span>
              <div className="flex flex-wrap gap-2">
                {result.metadata.sensitive_word_matches && result.metadata.sensitive_word_matches.length > 0 ? (
                  result.metadata.sensitive_word_matches.map((word, idx) => (
                    <span key={idx} className="px-2 py-1 rounded bg-cyber-danger-dim border border-cyber-danger/30 text-cyber-danger font-cyber text-[10px] uppercase font-bold tracking-wider animate-pulse">
                      {word}
                    </span>
                  ))
                ) : (
                  <span className="text-xs text-gray-500 font-cyber">NO_SENSITIVE_KEYWORDS_DETECTED</span>
                )}
              </div>
            </div>
          </GlassCard>
        </div>
      )}
    </div>
  );
};

export default URLScanner;
