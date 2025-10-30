// static/js/validation.js
document.addEventListener('DOMContentLoaded', function() {
  const senha = document.getElementById('senha');
  const senhaConf = document.getElementById('senha_conf');
  const form = document.getElementById('registerForm');

  function checkReqs(pw) {
    return {
      length: pw.length >= 6,
      upper: /[A-Z]/.test(pw),
      number: /\d/.test(pw),
      special: /[!@#$%^&*()_\-+=\[{\]};:'",<.>\/?\\|`~]/.test(pw)
    };
  }

  function updateUI(pw) {
    const r = checkReqs(pw);
    setClass('req-length', r.length);
    setClass('req-upper', r.upper);
    setClass('req-number', r.number);
    setClass('req-special', r.special);
  }

  function setClass(id, ok) {
    const el = document.getElementById(id);
    if(!el) return;
    el.classList.remove('valid','invalid');
    el.classList.add(ok ? 'valid' : 'invalid');
  }

  if (senha) {
    senha.addEventListener('input', function(e){
      updateUI(e.target.value);
    });
  }

  if (form) {
    form.addEventListener('submit', function(e){
      const pw = senha ? senha.value : '';
      const pwConf = senhaConf ? senhaConf.value : '';

      const r = checkReqs(pw);
      const allOk = r.length && r.upper && r.number && r.special;

      if(!allOk) {
        alert('Senha não atende aos requisitos mínimos (6 caracteres, 1 maiúscula, 1 número, 1 caractere especial).');
        e.preventDefault();
        return;
      }
      if(pw !== pwConf) {
        alert('Senha e Confirmação de Senha são diferentes.');
        e.preventDefault();
        return;
      }
      // se tudo ok, permitir envio (o servidor também valida)
    });
  }

  // também validação no login (exemplo: esconder caracteres já está no input type password)
});
