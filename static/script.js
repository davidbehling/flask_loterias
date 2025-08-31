function ordenar(colunaIndex) {
  const tabela = document.getElementById("sorteioTable");
  let linhas = Array.from(tabela.rows).slice(1);
  let ordemCrescente = tabela.dataset.ordem === "asc" ? false : true;

  linhas.sort((a, b) => {
    const valorA = a.cells[colunaIndex].innerText.trim();
    const valorB = b.cells[colunaIndex].innerText.trim();

    if (colunaIndex === 0) {
      // coluna de data
      const dataA = parseDateBR(valorA);
      const dataB = parseDateBR(valorB);
      return ordemCrescente ? dataA - dataB : dataB - dataA;
    } else {
      // coluna numérica ou texto
      const numA = parseFloat(valorA.replace(",", "."));
      const numB = parseFloat(valorB.replace(",", "."));

      if (!isNaN(numA) && !isNaN(numB)) {
        return ordemCrescente ? numA - numB : numB - numA;
      } else {
        return ordemCrescente
          ? valorA.localeCompare(valorB, undefined, { sensitivity: 'base' })
          : valorB.localeCompare(valorA, undefined, { sensitivity: 'base' });
      }
    }
  });

  tabela.dataset.ordem = ordemCrescente ? "asc" : "desc";
  const tbody = tabela.querySelector("tbody");
  linhas.forEach(linha => tbody.appendChild(linha));
}

function parseDateBR(dateStr) {
  const [dia, mes, ano] = dateStr.split("/").map(Number);
  return new Date(ano, mes - 1, dia);
}
