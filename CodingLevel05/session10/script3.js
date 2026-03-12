
function findVolumeCube() {
    const side = parseFloat(document.getElementById('side').value);
    const result = side*side*side;
    
    const resultMsg = 'The volume of a cube with side ' + side + ' is ' + result + '.';
    document.getElementById('result_volume_cube').innerHTML = resultMsg;
}
function findVolumeCuboid() {
    alert("Inside findVolumeCuboid()");
    const length = parseFloat(document.getElementById('length').value);
    alert("length:" + length);
    const breadth = parseFloat(document.getElementById('breadth').value);
    const height = parseFloat(document.getElementById('height_cuboid').value);
    const result = length*breadth*height;
    
    const resultMsg = 'The volume of a cuboid with length ' + length + ', breadth ' + breadth + ' and height ' + height +  ' is ' + result + '.';
    document.getElementById('result_volume_cuboid').innerHTML = resultMsg;
}
function findVolumeCone() {
    const radius = parseFloat(document.getElementById('radius_cone').value);
    const height = parseFloat(document.getElementById('height_cone').value);
    const rough_result = Math.PI*radius*radius*height;
    const result = rough_result.toFixed;

    const resultMsg = 'The volume of a cylinder with radius ' + radius + ' and height ' + height + ' is ' + result + '.';
    document.getElementById('result_volume_cylinder').innerHTML = resultMsg;
}
function findVolumeCylinder() {
    const radius = parseFloat(document.getElementById('radius_cylinder').value);
    const height = parseFloat(document.getElementById('height_cylinder').value);
    const rough_result = 1/3*Math.PI*radius*radius*height;
    const result = rough_result.toFixed;

    const resultMsg = 'The volume of a cone with radius ' + radius + ' and height ' + height + ' is ' + result + '.';
    document.getElementById('result_volume_cone').innerHTML = resultMsg;
}
function findVolumeSphere() {
    const radius = parseFloat(document.getElementById('radius_sphere').value);
    const rough_result = 4/3*Math.PI*radius*radius*radius;
    const result = rough_result.toFixed;

    const resultMsg = 'The volume of a sphere with radius ' + radius + ' is ' + result + '.';
    document.getElementById('result_volume_cube').innerHTML = resultMsg;
}
