import { useState } from 'react'

function TreeNode({ node, level = 0 }) {
  const [expanded, setExpanded] = useState(level === 0)
  const hasChildren = node.children && node.children.length > 0

  // Get color from metadata or parent
  const color = node.metadata_?.color || getColorForLevel(level)

  return (
    <div className="select-none">
      <div
        className={`flex items-center gap-2 py-1.5 px-2 rounded hover:bg-gray-100 cursor-pointer ${
          level === 0 ? 'font-semibold' : ''
        }`}
        style={{ paddingLeft: `${level * 20 + 8}px` }}
        onClick={() => hasChildren && setExpanded(!expanded)}
      >
        {/* Expand/collapse icon or bullet */}
        {hasChildren ? (
          <svg
            className={`w-4 h-4 text-gray-400 transition-transform ${expanded ? 'rotate-90' : ''}`}
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
          </svg>
        ) : (
          <span
            className="w-2 h-2 rounded-full ml-1"
            style={{ backgroundColor: color }}
          />
        )}

        {/* Color indicator for top-level */}
        {level === 0 && (
          <span
            className="w-3 h-3 rounded"
            style={{ backgroundColor: color }}
          />
        )}

        {/* Node name */}
        <span className={level === 0 ? 'text-gray-900' : 'text-gray-700'}>
          {node.name}
        </span>

        {/* Domain code badge for top-level */}
        {level === 0 && (
          <span className="text-xs text-gray-400 ml-2">
            {node.code}
          </span>
        )}
      </div>

      {/* Children */}
      {expanded && hasChildren && (
        <div>
          {node.children.map((child) => (
            <TreeNode key={child.id} node={child} level={level + 1} />
          ))}
        </div>
      )}
    </div>
  )
}

// Fallback colors based on depth
function getColorForLevel(level) {
  const colors = ['#6B7280', '#9CA3AF', '#D1D5DB']
  return colors[Math.min(level, colors.length - 1)]
}

export default TreeNode
