import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import GlassCard from '../components/GlassCard';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { Brain, Settings, AlertTriangle, ShieldCheck, Activity, Award } from 'lucide-react';

const ModelComparison = () => {
  const { token } = useAuth();
  const [activeModel, setActiveModel] = useState('Random Forest');
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');

  const modelMetrics = [
    { name: 'Logistic Regression', accuracy: 89.4, f1: 88.7, precision: 89.0, trainTime: '0.1s', desc: 'Linear boundary model. Fast execution, baseline reference.' },
    { name: 'Decision Tree', accuracy: 91.5, f1: 90.8, precision: 91.2, trainTime: '0.3s', desc: 'Splits features iteratively. High interpretability, prone to variance.' },
    { name: 'Random Forest', accuracy: 96.5, f1: 95.8, precision: 96.2, trainTime: '1.2s', desc: 'Ensemble forest model. Excellent performance across layout vectors.' },
    { name: 'SVM', accuracy: 94.2, f1: 93.5, precision: 94.0, trainTime: '4.1s', desc: 'Support Vector Machine. Solid performance, expensive training scale.' },
    { name: 'MLP', accuracy: 95.9, f1: 95.2, precision: 95.6, trainTime: '8.7s', desc: 'Multi-Layer Perceptron (Deep learning). Detects complex multi-tier dependencies.' },
    { name: 'XGBoost', accuracy: 97.8, f1: 97.4, precision: 97.6, trainTime: '3.4s', desc: 'Gradient boosted trees. Highest threat accuracy index, resource heavy.' }
  ];

  useEffect(() => {
    fetchActiveModel();
  }, [token]);

  const fetchActiveModel = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/models/active');
      if (response.ok) {
        const data = await response.json();
        setActiveModel(data.active_model);
      } else {
        throw new Error();
      }
    } catch (e) {
      console.warn("Backend offline, loading active model from local storage fallback");
      setActiveModel(localStorage.getItem('cg_active_model') || 'Random Forest');
    }
  };

  const handleModelChange = async (modelName) => {
    setLoading(true);
    setMessage('');
    try {
      const response = await fetch('http://localhost:8000/api/models/select', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(token ? { 'Authorization': `Bearer ${token}` } : {})
        },
        body: JSON.stringify({ model_name: modelName })
      });

      if (response.ok) {
        const data = await response.json();
        setActiveModel(data.active_model);
        setMessage(`SUCCESS: Classifier switched to ${data.active_model}`);
      } else {
        throw new Error();
      }
    } catch (err) {
      console.warn("Backend offline, updating local mock state");
      localStorage.setItem('cg_active_model', modelName);
      setActiveModel(modelName);
      setMessage(`SUCCESS: Dev Mode updated active classifier to ${modelName}`);
    } finally {
      setLoading(false);
      // clear message after 3 seconds
      setTimeout(() => setMessage(''), 4000);
    }
  };

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8 space-y-8 relative">
      <div className="absolute top-0 right-1/4 w-96 h-96 rounded-full bg-cyber-accent/5 blur-[120px] pointer-events-none" />

      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold tracking-tight text-white font-cyber text-glow-accent">
          MODEL_BENCHMARKS
        </h1>
        <p className="text-sm text-gray-400">
          Compare heuristics training matrices and toggle active classification algorithms in the engine.
        </p>
      </div>

      {/* Accuracy Bar Chart */}
      <GlassCard title="PERFORMANCE_EVALUATION_MATRIX">
        <div className="h-80 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart
              data={modelMetrics}
              margin={{ top: 20, right: 10, left: -20, bottom: 5 }}
            >
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(0, 240, 255, 0.05)" />
              <XAxis dataKey="name" stroke="rgba(255, 255, 255, 0.4)" tick={{ fontSize: 10, fontFamily: 'Share Tech Mono' }} />
              <YAxis stroke="rgba(255, 255, 255, 0.4)" tick={{ fontSize: 10, fontFamily: 'Share Tech Mono' }} domain={[80, 100]} />
              <Tooltip 
                contentStyle={{ backgroundColor: 'rgba(8, 9, 10, 0.95)', borderColor: 'rgba(0, 240, 255, 0.2)', color: '#fff', fontSize: 11, fontFamily: 'Share Tech Mono' }}
                itemStyle={{ color: '#fff' }}
              />
              <Legend wrapperStyle={{ fontSize: 11, fontFamily: 'Share Tech Mono', paddingTop: 10 }} />
              <Bar dataKey="accuracy" name="Accuracy (%)" fill="#00f0ff" radius={[4, 4, 0, 0]} />
              <Bar dataKey="f1" name="F1-Score (%)" fill="#ff0055" radius={[4, 4, 0, 0]} />
              <Bar dataKey="precision" name="Precision (%)" fill="#ffaa00" radius={[4, 4, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </GlassCard>

      {/* Success Alert */}
      {message && (
        <div className="flex items-center space-x-2 text-xs border border-cyber-success/30 bg-cyber-success-dim text-cyber-success p-3 rounded font-cyber">
          <ShieldCheck className="h-4 w-4" />
          <span>{message}</span>
        </div>
      )}

      {/* Model Selection Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {modelMetrics.map((model) => {
          const isActive = activeModel === model.name;
          return (
            <GlassCard 
              key={model.name}
              title={model.name.toUpperCase()}
              glow={isActive}
              className={`flex flex-col justify-between h-64 border transition-all ${
                isActive ? 'border-cyber-accent bg-cyber-accent-dim/10' : 'border-cyber-border/20'
              }`}
            >
              <div className="space-y-3">
                <p className="text-xs text-gray-400 h-10 overflow-hidden leading-relaxed">
                  {model.desc}
                </p>

                {/* Score Stats */}
                <div className="grid grid-cols-3 gap-2 border-y border-cyber-border/5 py-2 font-cyber text-xs">
                  <div>
                    <span className="text-[10px] text-gray-500 block uppercase">Accuracy</span>
                    <span className="text-white font-bold">{model.accuracy}%</span>
                  </div>
                  <div>
                    <span className="text-[10px] text-gray-500 block uppercase">F1_Score</span>
                    <span className="text-white font-bold">{model.f1}%</span>
                  </div>
                  <div>
                    <span className="text-[10px] text-gray-500 block uppercase">TrainTime</span>
                    <span className="text-cyber-accent">{model.trainTime}</span>
                  </div>
                </div>
              </div>

              <div className="mt-4">
                {isActive ? (
                  <div className="w-full flex items-center justify-center space-x-1.5 py-2 border border-cyber-accent bg-cyber-accent-dim/30 rounded text-xs font-cyber text-cyber-accent tracking-wider">
                    <Award className="h-4 w-4 animate-pulse" />
                    <span>[ACTIVE_DETECTOR]</span>
                  </div>
                ) : (
                  <button
                    onClick={() => handleModelChange(model.name)}
                    disabled={loading}
                    className="w-full py-2 border border-cyber-border/40 hover:border-cyber-accent hover:bg-cyber-accent-dim hover:text-cyber-accent rounded text-xs font-cyber text-gray-400 hover:text-white transition-all duration-300 tracking-wider disabled:opacity-50"
                  >
                    DEPLOY_CLASSIFIER
                  </button>
                )}
              </div>
            </GlassCard>
          );
        })}
      </div>
    </div>
  );
};

export default ModelComparison;
