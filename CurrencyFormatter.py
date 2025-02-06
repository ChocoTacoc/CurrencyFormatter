function formatCurrency(amount) {
    return `$${amount.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}`;
}

const amount = parseFloat(prompt("Enter an amount:"));
console.log("Formatted amount:", formatCurrency(amount));
