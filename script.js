// Seleciona os elementos necessários para as interações da página.
const barraProgresso = document.querySelector('.scroll-progress');
const botaoMenu = document.querySelector('.menu-toggle');
const navegacao = document.querySelector('.navigation');
const botaoTema = document.querySelector('.theme-toggle');
const cursorGlow = document.querySelector('.cursor-glow');

// Verifica preferências do usuário e do dispositivo antes de ligar os
// efeitos de mouse (parallax, tilt, brilho), evitando forçar movimento
// em quem prefere menos animação ou em telas sem cursor de precisão.
const prefereMenosMovimento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const temPonteiroFino = window.matchMedia('(pointer: fine)').matches;
const efeitosDeMouseAtivos = temPonteiroFino && !prefereMenosMovimento;

// Faz o brilho radial acompanhar o cursor por toda a página.
if (cursorGlow && efeitosDeMouseAtivos) {
  window.addEventListener('pointermove', (evento) => {
    cursorGlow.style.transform = `translate3d(${evento.clientX - 240}px, ${evento.clientY - 240}px, 0)`;
    cursorGlow.classList.add('active');
  }, { passive: true });

  document.addEventListener('pointerleave', () => cursorGlow.classList.remove('active'));
}

// Atualiza a largura da barra no topo conforme a página é rolada.
const atualizarBarraProgresso = () => {
  const alturaRolavel = document.documentElement.scrollHeight - window.innerHeight;
  const porcentagem = alturaRolavel ? (window.scrollY / alturaRolavel) * 100 : 0;
  if (barraProgresso) barraProgresso.style.width = `${porcentagem}%`;
};

window.addEventListener('scroll', atualizarBarraProgresso, { passive: true });
atualizarBarraProgresso();

// Abre e fecha o menu em telas menores.
if (botaoMenu && navegacao) {
  botaoMenu.addEventListener('click', () => {
    const menuAberto = navegacao.classList.toggle('open');
    botaoMenu.setAttribute('aria-expanded', String(menuAberto));
    botaoMenu.setAttribute(
      'aria-label',
      menuAberto ? 'Fechar menu' : 'Abrir menu',
    );
  });

  // Fecha o menu após a escolha de uma seção no celular.
  navegacao.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navegacao.classList.remove('open');
      botaoMenu.setAttribute('aria-expanded', 'false');
      botaoMenu.setAttribute('aria-label', 'Abrir menu');
    });
  });
}

// Move os orbs, o logotipo e o cartão de destaque do hero de acordo
// com a posição do cursor, criando um leve efeito de profundidade.
const secaoHero = document.querySelector('.hero');
const orbUm = document.querySelector('.orb-one');
const orbDois = document.querySelector('.orb-two');
const logoHero = document.querySelector('.hero-logo');
const cartaoDeScore = document.querySelector('.score-card');

if (secaoHero && efeitosDeMouseAtivos) {
  let quadroAgendado = false;
  let ultimoPonteiro = null;

  const aplicarParallaxDoHero = () => {
    quadroAgendado = false;
    if (!ultimoPonteiro) return;

    const area = secaoHero.getBoundingClientRect();
    const posX = (ultimoPonteiro.clientX - area.left) / area.width - 0.5;
    const posY = (ultimoPonteiro.clientY - area.top) / area.height - 0.5;

    if (orbUm) orbUm.style.transform = `translate3d(${posX * -30}px, ${posY * -30}px, 0)`;
    if (orbDois) orbDois.style.transform = `translate3d(${posX * 42}px, ${posY * 42}px, 0)`;
    if (logoHero) logoHero.style.transform = `translate3d(${posX * -18}px, ${posY * -18}px, 0)`;

    if (cartaoDeScore) {
      const inclinacaoX = posY * -8;
      const inclinacaoY = posX * 10;
      cartaoDeScore.style.transform =
        `rotate(3deg) translate3d(${posX * 10}px, ${posY * 10}px, 0) perspective(700px) rotateX(${inclinacaoX}deg) rotateY(${inclinacaoY}deg)`;
    }
  };

  secaoHero.addEventListener('pointermove', (evento) => {
    ultimoPonteiro = evento;
    if (!quadroAgendado) {
      quadroAgendado = true;
      requestAnimationFrame(aplicarParallaxDoHero);
    }
  }, { passive: true });

  secaoHero.addEventListener('pointerleave', () => {
    ultimoPonteiro = null;
    [orbUm, orbDois, logoHero].forEach((elemento) => {
      if (elemento) elemento.style.transform = '';
    });
    if (cartaoDeScore) cartaoDeScore.style.transform = 'rotate(3deg)';
  });
}

// Revela cada bloco suavemente quando ele entra na área visível da tela.
const elementosRevelaveis = document.querySelectorAll('.reveal');

// Calcula um atraso escalonado (stagger) para elementos que dividem o
// mesmo elemento-pai, em vez de depender de regras fixas por nth-child.
// Assim, qualquer grade ou lista da página ganha entrada em cascata.
const gruposPorPai = new Map();
elementosRevelaveis.forEach((elemento) => {
  const pai = elemento.parentElement;
  if (!gruposPorPai.has(pai)) gruposPorPai.set(pai, []);
  gruposPorPai.get(pai).push(elemento);
});
gruposPorPai.forEach((irmaos) => {
  irmaos.forEach((elemento, indice) => {
    elemento.style.setProperty('--reveal-delay', `${Math.min(indice, 5) * 0.09}s`);
  });
});

if ('IntersectionObserver' in window) {
  const observador = new IntersectionObserver((entradas) => {
    entradas.forEach((entrada) => {
      if (entrada.isIntersecting) {
        entrada.target.classList.add('visible');
        observador.unobserve(entrada.target);
      }
    });
  }, { threshold: 0.12 });

  elementosRevelaveis.forEach((elemento) => observador.observe(elemento));
} else {
  elementosRevelaveis.forEach((elemento) => elemento.classList.add('visible'));
}

// Anima os números da seção de impacto apenas uma vez, sem alterar valores textuais como infinito.
const animarNumero = (elemento) => {
  const destino = Number(elemento.dataset.counter);
  const inicio = performance.now();
  const duracao = 1100;

  const atualizar = (agora) => {
    const progresso = Math.min((agora - inicio) / duracao, 1);
    elemento.textContent = Math.floor(progresso * destino);
    if (progresso < 1) requestAnimationFrame(atualizar);
  };
  requestAnimationFrame(atualizar);
};

const secaoImpacto = document.querySelector('.stat-grid');
if (secaoImpacto && 'IntersectionObserver' in window) {
  const observadorImpacto = new IntersectionObserver((entradas) => {
    if (entradas[0].isIntersecting) {
      document.querySelectorAll('[data-counter]').forEach(animarNumero);
      observadorImpacto.disconnect();
    }
  }, { threshold: 0.45 });

  observadorImpacto.observe(secaoImpacto);
} else if (secaoImpacto) {
  document.querySelectorAll('[data-counter]').forEach((elemento) => {
    elemento.textContent = elemento.dataset.counter;
  });
}

// Vira o cartão de cada integrante ao clicar (ou usar Enter/Espaço) na foto,
// revelando o espaço reservado para o QR code do LinkedIn.
const cartoesEquipe = document.querySelectorAll('.member-photo');

const alternarCartao = (cartao) => {
  const virado = cartao.classList.toggle('flipped');
  cartao.setAttribute('aria-pressed', String(virado));
};

cartoesEquipe.forEach((cartao) => {
  cartao.addEventListener('click', () => alternarCartao(cartao));

  cartao.addEventListener('keydown', (evento) => {
    if (evento.key === 'Enter' || evento.key === ' ') {
      evento.preventDefault();
      alternarCartao(cartao);
    }
  });

  // O tilt atua no .member-photo (elemento pai), enquanto o flip de
  // clique continua rodando no .photo-flip (filho) — por isso os dois
  // efeitos convivem sem disputar a mesma propriedade transform.
  if (efeitosDeMouseAtivos) {
    cartao.addEventListener('pointermove', (evento) => {
      const area = cartao.getBoundingClientRect();
      const posX = (evento.clientX - area.left) / area.width - 0.5;
      const posY = (evento.clientY - area.top) / area.height - 0.5;
      cartao.style.transform = `perspective(900px) rotateX(${posY * -10}deg) rotateY(${posX * 12}deg)`;
    });

    cartao.addEventListener('pointerleave', () => {
      cartao.style.transform = '';
    });
  }
});