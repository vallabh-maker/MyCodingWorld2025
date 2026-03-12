function findSum() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const result = num1 + num2;

    const resultMsg = 'The sum of ' + num1 + ' and ' + num2 + ' is ' + result + '.';
    document.getElementById('result_sum').innerHTML = resultMsg
}
function findDifference() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const result = num1 - num2;

    const resultMsg = 'The difference between ' + num1 + ' and ' + num2 + ' is ' + result + '.';
    document.getElementById('result_difference').innerHTML = resultMsg
}
function findProduct() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const result = num1 * num2;

    const resultMsg = 'The product of ' + num1 + ' and ' + num2 + ' is ' + result + '.';
    document.getElementById('result_product').innerHTML = resultMsg
}
function findQuotient() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const result = num1 / num2;

    const resultMsg = 'The quotient when ' + num1 + ' is divided by ' + num2 + ' is ' + result + '.';
    document.getElementById('result_quotient').innerHTML = resultMsg
}
function findRemainder() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const result = num1 % num2;

    const resultMsg = 'The remainder when ' + num1 + ' is divided by ' + num2 + ' is ' + result + '.';
    document.getElementById('result_remainder').innerHTML = resultMsg
}