import { useState, useEffect } from 'react'

const API = 'http://localhost:8000'

export default function App() {
  const [teams, setTeams] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch(`${API}/teams`)
      .then(r => r.json())
      .then(data => { setTeams(data); setLoading(false) })
      .catch(e => { setError(e.message); setLoading(false) })
  }, [])

  return (
    <div style={{ fontFamily: 'sans-serif', maxWidth: 720, margin: '0 auto', padding: '2rem' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1.5rem' }}>
        <span style={{ fontSize: '2rem' }}>🏆</span>
        <h1 style={{ margin: 0, color: '#1e293b' }}>Liga Española</h1>
        <span style={{ marginLeft: 'auto', background: '#2496ED', color: 'white', borderRadius: 9999, padding: '0.2rem 0.8rem', fontSize: '0.8rem' }}>
          {teams.length} equipos
        </span>
      </div>

      {loading && <p style={{ color: '#64748b' }}>Cargando equipos...</p>}
      {error   && <p style={{ color: '#dc2626' }}>Error: {error}</p>}

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '1rem' }}>
        {teams.map(t => (
          <div key={t.id} style={{
            background: 'white',
            border: '1px solid #e2e8f0',
            borderRadius: 12,
            padding: '1rem 1.2rem',
            boxShadow: '0 2px 8px rgba(0,0,0,0.06)',
          }}>
            <strong style={{ color: '#1e293b', fontSize: '1rem' }}>{t.name}</strong>
            <p style={{ margin: '0.3rem 0 0', color: '#64748b', fontSize: '0.85rem' }}>📍 {t.city}</p>
            <p style={{ margin: '0.15rem 0 0', color: '#64748b', fontSize: '0.85rem' }}>🏟️ {t.stadium}</p>
            <p style={{ margin: '0.15rem 0 0', color: '#94a3b8', fontSize: '0.78rem' }}>Fundado en {t.founded}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
