import { useState, useEffect } from 'react'
import { getDomainChildren } from '../api/client'

function DomainCard({ domain }) {
  const [children, setChildren] = useState([])
  const [expanded, setExpanded] = useState(false)

  const color = domain.metadata_?.color || '#6B7280'

  useEffect(() => {
    if (expanded && children.length === 0) {
      getDomainChildren(domain.code).then(setChildren)
    }
  }, [expanded, domain.code, children.length])

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
      {/* Header with color bar */}
      <div
        className="h-2"
        style={{ backgroundColor: color }}
      />

      <div className="p-5">
        {/* Domain name */}
        <h3 className="text-lg font-semibold text-gray-900 mb-2">
          {domain.name}
        </h3>

        {/* Description */}
        <p className="text-gray-600 text-sm mb-4">
          {domain.description}
        </p>

        {/* Expand button */}
        <button
          onClick={() => setExpanded(!expanded)}
          className="text-sm font-medium flex items-center gap-1 transition-colors"
          style={{ color: color }}
        >
          <span>{expanded ? 'Hide' : 'Show'} subdomains</span>
          <svg
            className={`w-4 h-4 transition-transform ${expanded ? 'rotate-180' : ''}`}
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </button>

        {/* Subdomains list */}
        {expanded && children.length > 0 && (
          <div className="mt-4 pt-4 border-t border-gray-100">
            <ul className="space-y-2">
              {children.map((child) => (
                <li
                  key={child.id}
                  className="text-sm text-gray-700 flex items-center gap-2"
                >
                  <span
                    className="w-2 h-2 rounded-full"
                    style={{ backgroundColor: color }}
                  />
                  {child.name}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  )
}

export default DomainCard
