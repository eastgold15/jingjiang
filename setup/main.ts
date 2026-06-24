import { defineAppSetup } from '@slidev/types'
import AtomBox from '../components/atoms/AtomBox.vue'
import AtomFlex from '../components/atoms/AtomFlex.vue'
import AtomText from '../components/atoms/AtomText.vue'
import AtomBadge from '../components/atoms/AtomBadge.vue'
import AtomBtn from '../components/atoms/AtomBtn.vue'
import AtomDivider from '../components/atoms/AtomDivider.vue'

export default defineAppSetup(({ app }) => {
  const atoms = { AtomBox, AtomFlex, AtomText, AtomBadge, AtomBtn, AtomDivider }
  Object.entries(atoms).forEach(([name, comp]) => app.component(name, comp))
})
