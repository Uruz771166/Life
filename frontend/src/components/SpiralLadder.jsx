import StageCard from './StageCard'

function SpiralLadder({ stages }) {
  // Reverse to show TURQUOISE at top, BEIGE at bottom
  const reversedStages = [...stages].reverse()

  return (
    <div className="space-y-4">
      {reversedStages.map((stage, index) => (
        <StageCard
          key={stage.id}
          stage={stage}
          isFirst={index === 0}
          isLast={index === reversedStages.length - 1}
        />
      ))}
    </div>
  )
}

export default SpiralLadder
