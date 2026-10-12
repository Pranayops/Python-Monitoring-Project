let cart = [];
const count = document.getElementById('cartCount');
const toast = document.getElementById('toast');
let toastTimer;
function showToast(message){toast.textContent=message;toast.classList.add('show');clearTimeout(toastTimer);toastTimer=setTimeout(()=>toast.classList.remove('show'),2400)}
document.querySelectorAll('.add-button').forEach(button=>button.addEventListener('click',()=>{cart.push(button.dataset.product);count.textContent=cart.length;showToast(`${button.dataset.product} added to your demo bag ✨`)}));
document.getElementById('cartButton').addEventListener('click',()=>{if(!cart.length){showToast('Your bag is empty — pick your favourite first.');return}const summary=cart.reduce((acc,item)=>(acc[item]=(acc[item]||0)+1,acc),{});showToast('Demo bag: '+Object.entries(summary).map(([name,qty])=>`${name} ×${qty}`).join(' · '))});
