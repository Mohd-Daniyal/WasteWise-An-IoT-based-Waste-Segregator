async function updateCameraFeed() {
    try {
        const response = await fetch('/camera_feed');
        const imageData = await response.blob();
        const imageUrl = URL.createObjectURL(imageData);
        document.getElementById('camera-feed').src = imageUrl;
    } catch (error) {
        console.error('Error fetching camera feed:', error);
    }
}

setInterval(updateCameraFeed, 1000);
updateCameraFeed();

async function classifyWaste() {
    try {
        const response = await fetch('/classify', { method: 'POST' });
        const data = await response.json();
        const result = data.category;
        document.getElementById('classification-result').innerText = `The waste on the lid is ${result}`;
        console.log('Data from classify endpoint:', data);
        
        document.getElementById('dump-btn').style.display = 'block';
    } catch (error) {
        console.error('Error classifying waste:', error);
        document.getElementById('classification-result').innerText = 'Error classifying waste';
    }
}

async function dumpWaste() {
    const result = document.getElementById('classification-result').innerText.split(" ").pop();
    try {
        const response = await fetch('/dump', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ category: result })
        });

        if (response.ok) {
            console.log('Waste dumped successfully!');
            document.getElementById('dump-btn').style.display = 'none';
            document.getElementById('classification-result').innerText = '';
        } else {
            console.error('Failed to dump waste:', response.statusText);
        }
    } catch (error) {
        console.error('Error dumping waste:', error);
    }
}

document.getElementById('classify-btn').addEventListener('click', classifyWaste);
document.getElementById('dump-btn').addEventListener('click', dumpWaste);