// The bot's day bookkeeping. Day shutoffs clear each morning; the 2-of-10 review hold stays until you clear it.
const START = 1000; // dry run paper balance to start (live sizes to Public's buying power)

function freshState() {
  return { balance: START, trades: [], last10: [], day: null, halt: null, reviewHold: null };
}

function newDay(st, day) {
  if (st.day === day) return false;
  st.day = day;
  st.halt = null;
  st.dayStart = st.balance;
  st.dayBest = 0;
  return true;
}

module.exports = { freshState, newDay, START };
