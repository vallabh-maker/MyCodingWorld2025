const results = [
    ["Shriya Narayan R", "Vibgyor High School", 100],
    ["Devanarayan R", "Gopalan National School", 100],
    ["Dyuthi Bhatraju", "Baldwin Girls High School", 100],
    ["Anviksha Surana", "Vibgyor High School", 100],
    ["Vedika Gotur", "Ryan International School", 100]
];

function displayResults() {
    alert('1');
    const resultsDiv = document.getElementById('results');
    let html = '';
    html = `${html}<table border = '1' width = '100%'>`;
    alert('2');
    html = `${html}<tr>
    <th>Sl. No.</th>
    <th>Name</th>
    <th>School</th>
    <th>Score</th>
    </tr>`;
    
    for(let i = 0; i < results.length; i++) {
        html = html + '<tr>';
        html = `${html}<td>${i+1}</td>`;

        for(let j = 0; j < results[i].length; j++) {
            html = `${html}<td>${results[i][j]}</td>`;
        }

        html = `${html}</tr>`;
    }



    html = `${html}</table>`;

    resultsDiv.innerHTML = html;
}