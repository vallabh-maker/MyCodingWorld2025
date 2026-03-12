
function findAreaSquare() {
    const side = parseFloat(document.getElementById('side').value);
    const result = side*side;
    
    const resultMsg = 'The area of a square with side ' + side + ' is ' + result + '.';
    document.getElementById('result_area_square').innerHTML = resultMsg;
}
function findAreaRectangle() {
    const length = parseFloat(document.getElementById('length').value);
    const breadth = parseFloat(document.getElementById('breadth').value);
    const result = length*breadth;
    
    const resultMsg = 'The area of a rectangle with length ' + length + ' and breadth ' + breadth + ' is ' + result + '.';
    document.getElementById('result_area_rectangle').innerHTML = resultMsg;
}
function findAreaTriangle() {
    const base = parseFloat(document.getElementById('base').value);
    const height = parseFloat(document.getElementById('height').value);
    const result = 1/2*base*height;
    
    const resultMsg = 'The area of a triangle with base ' + base + ' and height ' + height + ' is ' + result + '.';
    document.getElementById('result_area_triangle').innerHTML = resultMsg;
}
function findAreaCircle() {
    const radius = parseFloat(document.getElementById('radius').value);
    const rough_result = Math.PI*radius*radius;
    result = rough_result.toFixed(2);
    
    const resultMsg = 'The area of a circle with radius ' + radius + ' is ' + result + '.';
    document.getElementById('result_area_circle').innerHTML = resultMsg;
}
