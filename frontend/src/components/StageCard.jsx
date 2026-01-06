import { useState } from 'react'

function StageCard({ stage, isFirst, isLast }) {
  const [expanded, setExpanded] = useState(false)

  const { characteristics } = stage

  // Determine text color based on background brightness
  const textColor = isLightColor(stage.color) ? 'text-gray-900' : 'text-white'

  return (
    <div className="relative">
      {/* Connector line */}
      {!isLast && (
        <div
          className="absolute left-8 top-full w-0.5 h-4 z-0"
          style={{ backgroundColor: stage.color }}
        />
      )}

      <div
        className="rounded-lg shadow-md overflow-hidden cursor-pointer transition-all hover:shadow-lg"
        onClick={() => setExpanded(!expanded)}
      >
        {/* Header */}
        <div
          className="p-4 flex items-center gap-4"
          style={{ backgroundColor: stage.color }}
        >
          {/* Stage indicator */}
          <div className={`w-12 h-12 rounded-full bg-white/20 flex items-center justify-center ${textColor}`}>
            <span className="text-lg font-bold">{stage.ordinal + 1}</span>
          </div>

          <div className="flex-1">
            <h3 className={`font-bold text-lg ${textColor}`}>
              {stage.code}
            </h3>
            <p className={`text-sm opacity-90 ${textColor}`}>
              {stage.name}
            </p>
          </div>

          {/* Expand icon */}
          <svg
            className={`w-5 h-5 transition-transform ${expanded ? 'rotate-180' : ''} ${textColor}`}
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </div>

        {/* Expanded content */}
        {expanded && (
          <div className="p-4 bg-white border-t">
            {/* Description */}
            <p className="text-gray-700 mb-4">{stage.description}</p>

            {/* Worldview */}
            {characteristics?.worldview && (
              <div className="mb-4">
                <h4 className="font-semibold text-gray-900 mb-1">Worldview</h4>
                <p className="text-gray-600 text-sm">{characteristics.worldview}</p>
              </div>
            )}

            {/* Core Values */}
            {characteristics?.core_values && (
              <div className="mb-4">
                <h4 className="font-semibold text-gray-900 mb-2">Core Values</h4>
                <div className="flex flex-wrap gap-2">
                  {characteristics.core_values.map((value, i) => (
                    <span
                      key={i}
                      className="px-2 py-1 text-xs rounded-full"
                      style={{
                        backgroundColor: `${stage.color}20`,
                        color: stage.color,
                      }}
                    >
                      {value}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {/* Motivations */}
            {characteristics?.motivations && (
              <div className="mb-4">
                <h4 className="font-semibold text-gray-900 mb-1">Motivations</h4>
                <ul className="text-gray-600 text-sm list-disc list-inside">
                  {characteristics.motivations.map((item, i) => (
                    <li key={i}>{item}</li>
                  ))}
                </ul>
              </div>
            )}

            {/* Fears */}
            {characteristics?.fears && (
              <div className="mb-4">
                <h4 className="font-semibold text-gray-900 mb-1">Fears</h4>
                <ul className="text-gray-600 text-sm list-disc list-inside">
                  {characteristics.fears.map((item, i) => (
                    <li key={i}>{item}</li>
                  ))}
                </ul>
              </div>
            )}

            {/* Typical Behaviors */}
            {characteristics?.typical_behaviors && (
              <div className="mb-4">
                <h4 className="font-semibold text-gray-900 mb-1">Typical Behaviors</h4>
                <ul className="text-gray-600 text-sm list-disc list-inside">
                  {characteristics.typical_behaviors.map((item, i) => (
                    <li key={i}>{item}</li>
                  ))}
                </ul>
              </div>
            )}

            {/* Transition Triggers */}
            {characteristics?.transition_triggers && (
              <div>
                <h4 className="font-semibold text-gray-900 mb-1">Transition Triggers</h4>
                <ul className="text-gray-600 text-sm list-disc list-inside">
                  {characteristics.transition_triggers.map((item, i) => (
                    <li key={i}>{item}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  )
}

// Helper to determine if a color is light
function isLightColor(hex) {
  const r = parseInt(hex.slice(1, 3), 16)
  const g = parseInt(hex.slice(3, 5), 16)
  const b = parseInt(hex.slice(5, 7), 16)
  const luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
  return luminance > 0.5
}

export default StageCard
