document.getElementById('interest-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const principal = parseFloat(document.getElementById('principal').value);
    
    console.log(principal)
    
    const rate = parseFloat(document.getElementById('rate').value);
    
    console.log(rate)
    
    const years = parseInt(document.getElementById('years').value);
    
    document.getElementById("outputprincipal").textContent = name;
    document.getElementById("outputrate").textContent = email;

    

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `Interest earned: $${interest.toFixed(2)}`;
    
});
