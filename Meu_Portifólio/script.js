const dadosPortefolio = {
  competencias: [
    { icone: "🛠", titulo: "Hardware", descricao: "Diagnóstico de computadores." },
    { icone: "⌘", titulo: "Redes", descricao: "TCP/IP, configuração, conectividade e redes locais." },
    { icone: "▣", titulo: "Sistemas", descricao: "Windows, Linux, instalação." },
    { icone: '&lt/&gt', titulo: "Desenvolvimento Web", descricao: "HTML, CSS, JavaScript, React e APIs." }
  ],  
  projetos: [
    { imagem: "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=700&q=80", titulo: "Manutenção de Computadores", descricao: "Diagnóstico, limpeza, instalação e optimização de computadores.", etiquetas: "Hardware • Windows" },
    { imagem: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=700&q=80", titulo: "Infraestrutura de Rede Local", descricao: "Planeamento de rede local, cablagem, configuração e documentação.", etiquetas: "Redes • TCP/IP" },
    { imagem: "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=700&q=80", titulo: "Portfólio Web", descricao: "Website responsivo desenvolvido para apresentar competências e projectos.", etiquetas: "HTML • CSS • JavaScript" }
  ],
  experiencias: [
    { data: "2025 — ACTUAL", titulo: "Técnico de Informática / Estudante", descricao: "Formação e prática em suporte técnico, redes, desenvolvimento web e sistemas de informação." },
    { data: "PROJECTOS • FREELANCE", titulo: "Projectos e desenvolvimento", descricao: "Desenvolvimento de aplicações e experiências práticas em programação, web e infraestrutura." }
  ]
};

function escaparHtml(valor) {
  return String(valor).replace(/[&<>"']/g, caractere => ({ "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#039;" }[caractere]));
}

function mostrarCompetencias() {
  document.querySelector("#grelha-competencias").innerHTML = dadosPortefolio.competencias.map(competencia => `
    <article class="cartao-competencia">
      <div class="icone-competencia">${competencia.icone}</div>
      <div class="titulo-competencia">${escaparHtml(competencia.titulo)}</div>
      <div class="descricao-competencia">${escaparHtml(competencia.descricao)}</div>
    </article>
  `).join("");
}

function mostrarProjetos() {
  document.querySelector("#grelha-projetos").innerHTML = dadosPortefolio.projetos.map((projeto, indice) => `
    <article class="cartao-projeto">
      <div class="imagem-projeto"><img src="${projeto.imagem}" alt="${escaparHtml(projeto.titulo)}"></div>
      <div class="corpo-projeto">
        <div class="numero-projeto">${String(indice + 1).padStart(2, "0")} / PROJECTO</div>
        <div class="titulo-projeto">${escaparHtml(projeto.titulo)}</div>
        <div class="descricao-projeto">${escaparHtml(projeto.descricao)}</div>
        <div class="etiquetas-projeto">${escaparHtml(projeto.etiquetas)}</div>
      </div>
    </article>
  `).join("");
}

function mostrarExperiencias() {
  document.querySelector("#linha-experiencias").innerHTML = dadosPortefolio.experiencias.map(experiencia => `
    <article class="item-experiencia">
      <span class="ponto-experiencia"></span>
      <div class="data-experiencia">${escaparHtml(experiencia.data)}</div>
      <div class="titulo-experiencia">${escaparHtml(experiencia.titulo)}</div>
      <div class="descricao-experiencia">${escaparHtml(experiencia.descricao)}</div>
    </article>
  `).join("");
}

document.addEventListener("DOMContentLoaded", () => {
  mostrarCompetencias();
  mostrarProjetos();
  mostrarExperiencias();
  document.querySelector("#ano-atual").textContent = new Date().getFullYear();

  const botaoMenu = document.querySelector(".botao-menu");
  const barraNavegacao = document.querySelector(".barra-navegacao");
  botaoMenu.addEventListener("click", () => barraNavegacao.classList.toggle("menu-aberto"));

  document.querySelectorAll(".links-navegacao a").forEach(link => {
    link.addEventListener("click", () => barraNavegacao.classList.remove("menu-aberto"));
  });

  document.querySelector("#formulario-contacto").addEventListener("submit", evento => {
    evento.preventDefault();
    alert("Formulário de demonstração. Ligue este formulário a um backend ou serviço de formulários para receber mensagens.");
  });
});
