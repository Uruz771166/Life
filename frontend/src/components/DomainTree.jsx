import TreeNode from './TreeNode'

function DomainTree({ domains }) {
  return (
    <div className="bg-white rounded-lg shadow-sm border p-4">
      {domains.map((domain) => (
        <TreeNode key={domain.id} node={domain} level={0} />
      ))}
    </div>
  )
}

export default DomainTree
