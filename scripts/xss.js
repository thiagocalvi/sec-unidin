// Altera todas as nota do aluno de id 4 para 10, considera que o id do aluno não é individual por disciplina
(() => {
  const baseUrl = window.location.origin
  const pathAtual = window.location.pathname
  const segmentos = pathAtual.split('/').filter(Boolean)
  const idDisciplina = segmentos[segmentos.length - 1]
  const idStudent = 4
  const quantNotas = 4
  const nota = 10

  for (let i = 0; i < quantNotas; i++) {
    const endpoint = `/disciplina/${idDisciplina}/nota?student_id=${idStudent}&assessment=${i + 1}&value=${nota}`
    const url = `${baseUrl}${endpoint}`

    fetch(url, {
      method: 'GET',
      headers: {
        'Accept': 'application/json'
      }
    })
  }
})()
