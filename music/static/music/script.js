// ============================================
// Script principal - Music API
// Animações, validações e efeitos visuais
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ==========================================
    // 1. ANIMAÇÕES DE ENTRADA
    // ==========================================
    
    // Animar cards ao carregar
    const cards = document.querySelectorAll('.card, .result-card, .playlist-item, .musica-item');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 50);
    });

    // Animar colunas ao carregar
    const colunas = document.querySelectorAll('.coluna');
    colunas.forEach((coluna, index) => {
        coluna.style.opacity = '0';
        coluna.style.transform = 'scale(0.95)';
        coluna.style.transition = 'opacity 0.7s ease, transform 0.7s ease';
        
        setTimeout(() => {
            coluna.style.opacity = '1';
            coluna.style.transform = 'scale(1)';
        }, index * 100);
    });

    // ==========================================
    // 2. HOVER EFFECTS MELHORADOS
    // ==========================================
    
    // Efeito glow em botões ao hover
    const buttons = document.querySelectorAll('button, .btn, a[class*="btn"]');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.boxShadow = '0 8px 16px rgba(0, 0, 0, 0.2)';
            this.style.transform = 'scale(1.05)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.boxShadow = 'none';
            this.style.transform = 'scale(1)';
        });
    });

    // Animação ao hover em cards
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px)';
            this.style.boxShadow = '0 12px 24px rgba(0, 0, 0, 0.15)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '';
        });
    });

    // ==========================================
    // 3. MODAL DE CONFIRMAÇÃO PARA DELETAR
    // ==========================================
    
    const deleteLinks = document.querySelectorAll('a[href*="/deletar/"]');
    deleteLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            showDeleteModal(this.href);
        });
    });

    function showDeleteModal(deleteUrl) {
        // Crear modal overlay
        const overlay = document.createElement('div');
        overlay.className = 'modal-overlay';
        overlay.innerHTML = `
            <div class="modal-content">
                <div class=\"modal-icon\">!</div>
                <h2>Tem certeza?</h2>
                <p>Esta ação não pode ser desfeita</p>
                <div class="modal-buttons">
                    <button class="modal-cancel">Cancelar</button>
                    <button class="modal-confirm">Sim, Deletar</button>
                </div>
            </div>
        `;
        
        document.body.appendChild(overlay);
        
        // Animação de entrada
        setTimeout(() => {
            overlay.classList.add('show');
        }, 10);
        
        // Eventos dos botões
        overlay.querySelector('.modal-cancel').addEventListener('click', function() {
            overlay.classList.remove('show');
            setTimeout(() => overlay.remove(), 300);
        });
        
        overlay.querySelector('.modal-confirm').addEventListener('click', function() {
            overlay.classList.remove('show');
            setTimeout(() => {
                window.location.href = deleteUrl;
            }, 300);
        });
        
        // Fechar ao clicar fora
        overlay.addEventListener('click', function(e) {
            if (e.target === overlay) {
                overlay.classList.remove('show');
                setTimeout(() => overlay.remove(), 300);
            }
        });
    }

    // ==========================================
    // 4. VALIDAÇÃO DE FORMULÁRIOS
    // ==========================================
    
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const inputs = this.querySelectorAll('input[required], textarea[required], select[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (input.value.trim() === '') {
                    isValid = false;
                    input.classList.add('input-error');
                    
                    // Remover erro ao digitar
                    input.addEventListener('input', function() {
                        this.classList.remove('input-error');
                    });
                } else {
                    input.classList.remove('input-error');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showNotification('Por favor, preencha todos os campos obrigatórios', 'error');
            }
        });
    });

    // ==========================================
    // 5. NOTIFICAÇÕES COM TOAST
    // ==========================================
    
    function showNotification(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.innerHTML = `
            <span>${message}</span>
            <button class="toast-close">&times;</button>
        `;
        
        document.body.appendChild(toast);
        
        // Animação de entrada
        setTimeout(() => {
            toast.classList.add('show');
        }, 10);
        
        // Fechar manual
        toast.querySelector('.toast-close').addEventListener('click', function() {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        });
        
        // Fechar automático
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 4000);
    }

    // ==========================================
    // 6. FEEDBACK AO SUBMETER FORMULÁRIOS
    // ==========================================
    
    forms.forEach(form => {
        if (!form.classList.contains('submit-feedback-added')) {
            form.classList.add('submit-feedback-added');
            
            form.addEventListener('submit', function(e) {
                // Apenas se o formulário é válido
                if (this.checkValidity() === false) return;
                
                const submitBtn = this.querySelector('button[type="submit"]');
                if (submitBtn) {
                    const originalText = submitBtn.textContent;
                    submitBtn.textContent = '⏳ Salvando...';
                    submitBtn.disabled = true;
                    submitBtn.style.opacity = '0.6';
                    
                    // Restaurar após envio
                    setTimeout(() => {
                        submitBtn.textContent = originalText;
                        submitBtn.disabled = false;
                        submitBtn.style.opacity = '1';
                    }, 2000);
                }
            });
        }
    });

    // ==========================================
    // 7. BUSCA E FILTRO COM DEBOUNCE
    // ==========================================
    
    const searchInputs = document.querySelectorAll('input[type="text"][placeholder*="Buscar"]');
    searchInputs.forEach(input => {
        let debounceTimer;
        
        input.addEventListener('input', function() {
            clearTimeout(debounceTimer);
            
            const query = this.value.trim();
            if (query.length === 0) return;
            
            debounceTimer = setTimeout(() => {
                // Mostrar indicador de busca
                this.style.borderColor = '#FFD93D';
                this.style.boxShadow = '0 0 0 3px rgba(255, 217, 61, 0.2)';
            }, 300);
        });
    });

    // ==========================================
    // 8. SCROLL SUAVE PARA LINKS INTERNOS
    // ==========================================
    
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // ==========================================
    // 9. LOADING STATE PARA LINKS DE AÇÃO
    // ==========================================
    
    document.querySelectorAll('a:not([href^="#"])').forEach(link => {
        link.addEventListener('click', function() {
            // Não adicionar em links de deleção (já tem modal)
            if (!this.href.includes('/deletar/')) {
                this.style.opacity = '0.5';
                this.style.pointerEvents = 'none';
            }
        });
    });

    // ==========================================
    // 10. EFEITO AO FOCAR EM INPUTS
    // ==========================================
    
    const inputs = document.querySelectorAll('input, textarea, select');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.style.borderColor = '#FFD93D';
            this.style.boxShadow = '0 0 0 3px rgba(255, 217, 61, 0.2)';
            this.parentElement.style.transform = 'scale(1.02)';
        });
        
        input.addEventListener('blur', function() {
            this.style.borderColor = '#FFD93D';
            this.style.boxShadow = 'none';
            this.parentElement.style.transform = 'scale(1)';
        });
    });

    // ==========================================
    // 11. PROGRESSO DE CARREGAMENTO DE PÁGINA
    // ==========================================
    
    if (document.readyState === 'loading') {
        showLoadingBar();
    }
    
    function showLoadingBar() {
        const progressBar = document.createElement('div');
        progressBar.className = 'progress-bar';
        document.body.appendChild(progressBar);
        
        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 30;
            progress = Math.min(progress, 90);
            progressBar.style.width = progress + '%';
            
            if (document.readyState === 'complete') {
                clearInterval(interval);
                progress = 100;
                progressBar.style.width = progress + '%';
                setTimeout(() => {
                    progressBar.style.opacity = '0';
                    setTimeout(() => progressBar.remove(), 300);
                }, 500);
            }
        }, 200);
    }

    // ==========================================
    // 12. CONTADORES COM ANIMAÇÃO
    // ==========================================
    
    const counters = document.querySelectorAll('[data-count]');
    counters.forEach(counter => {
        const target = parseInt(counter.dataset.count);
        let current = 0;
        const increment = target / 20;
        
        const updateCounter = () => {
            if (current < target) {
                current += increment;
                counter.textContent = Math.ceil(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };
        
        updateCounter();
    });

    console.log('Music API - JavaScript initialized!');
});

// ============================================
// ESTILOS DINÂMICOS (injetados via JS)
// ============================================

const style = document.createElement('style');
style.textContent = `
/* Modal de Confirmação */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.modal-overlay.show {
    opacity: 1;
}

.modal-content {
    background: #2a2a2a;
    padding: 2rem;
    border-radius: 12px;
    text-align: center;
    max-width: 400px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
    transform: scale(0.7);
    transition: transform 0.3s ease;
    border: 2px solid #FFD93D;
}

.modal-overlay.show .modal-content {
    transform: scale(1);
}

.modal-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.modal-content h2 {
    color: #FFD93D;
    margin-bottom: 0.5rem;
}

.modal-content p {
    color: #b0b0b0;
    margin-bottom: 1.5rem;
}

.modal-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
}

.modal-buttons button {
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

.modal-cancel {
    background-color: #505050;
    color: #FFD93D;
}

.modal-cancel:hover {
    background-color: #FFD93D;
    color: #0f0f0f;
}

.modal-confirm {
    background-color: #FFD93D;
    color: #0f0f0f;
}

.modal-confirm:hover {
    background-color: #FFA500;
}

/* Toast Notifications */
.toast {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    background: #2a2a2a;
    padding: 1rem 1.5rem;
    border-radius: 8px;
    box-shadow: 0 8px 24px rgba(255, 217, 61, 0.2);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    max-width: 400px;
    transform: translateX(500px);
    transition: transform 0.3s ease;
    z-index: 999;
    color: #f0f0f0;
}

.toast.show {
    transform: translateX(0);
}

.toast-info {
    border-left: 4px solid #FFD93D;
}

.toast-success {
    border-left: 4px solid #FFD93D;
}

.toast-error {
    border-left: 4px solid #FFD93D;
}

.toast-close {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #FFD93D;
    transition: color 0.2s ease;
}

.toast-close:hover {
    color: #FFA500;
}

/* Input Error */
.input-error {
    border-color: #FFD93D !important;
    background-color: #3a2a1a !important;
}

/* Progress Bar */
.progress-bar {
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: linear-gradient(90deg, #FFD93D, #FFA500, #FFD93D);
    width: 0;
    z-index: 9999;
    transition: width 0.3s ease;
    opacity: 1;
}

/* Transições suaves para hover */
button, a {
    transition: all 0.3s ease !important;
}

/* Responsiveidade */
@media (max-width: 480px) {
    .modal-content {
        max-width: 90%;
    }
    
    .toast {
        bottom: 1rem;
        right: 1rem;
        left: 1rem;
        max-width: none;
    }
    
    .modal-buttons {
        flex-direction: column;
    }
}
`;

document.head.appendChild(style);
