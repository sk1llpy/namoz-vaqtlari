let API_DOMAIN = 'https://3587-84-54-66-106.ngrok-free.app';
let tg = window.Telegram.WebApp;

tg.expand();

const urlParams = new URLSearchParams(window.location.search);
const userId = urlParams.get('user_id');

if (userId === null) {
    var user_id = tg.initDataUnsafe.user.id;
} else {
    var user_id = userId;
    var link = document.getElementById('home_a');
    link.href = `${API_DOMAIN}/main?user_id=${user_id}`;

    var link_zikr = document.getElementById('zikr_a');
    link_zikr.href = `${API_DOMAIN}/main?user_id=${user_id}`;

    var link_tasbih = document.getElementById('tasbih_a');
    link_tasbih.href = `${API_DOMAIN}?user_id=${user_id}`;
}


fetch(`${API_DOMAIN}/api/users/get/`, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        'user_id': user_id
    })
})
.then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
})
.then(data => {
    let response_data = JSON.stringify(data.tasbih);
    let response_mode = JSON.stringify(data.mode);
    
    document.getElementById("count").innerText = response_data; // Use assignment operator "="

    if (parseInt(response_mode) !== 999999) {
        document.getElementById("max-count").innerText = response_mode; // Use assignment operator "="
    } else {
        document.getElementById("max-count").innerText = response_mode; // Use assignment operator "="
        document.getElementById("max-count").style.display = 'none'; // Use assignment operator "="
    };
})
.catch(error => {
    console.error('There was a problem with the fetch request:', error);
});


function increaseNumber() {
    const numberText = document.getElementById("count").innerText;
    const intNumber = parseInt(numberText);
    const max_count = parseInt(document.getElementById("max-count").innerText);


    if (max_count == intNumber){
        const newNumber = 1;
        document.getElementById("count").innerText = newNumber;

        fetch(`${API_DOMAIN}/api/tasbih/update/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'user_id': user_id,
                'count': newNumber
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(JSON.stringify(data)); // Display data in an console.log dialog
        })
        .catch(error => {
            console.error('There was a problem with the fetch request:', error);
        });
        
    } else {
        const newNumber = intNumber + 1;
        document.getElementById("count").innerText = newNumber;

        fetch(`${API_DOMAIN}/api/tasbih/update/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'user_id': user_id,
                'count': newNumber
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(JSON.stringify(data)); // Display data in an console.log dialog
        })
        .catch(error => {
            console.error('There was a problem with the fetch request:', error);
        });

    };
}

function decreaseNumber() {
    const numberText = document.getElementById("count").innerText;
    const intNumber = parseInt(numberText);
    const max_count = parseInt(document.getElementById("max-count").innerText);

    if (0 != intNumber){
        const newNumber = intNumber - 1;
        document.getElementById("count").innerText = newNumber;

        fetch(`${API_DOMAIN}/api/tasbih/update/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'user_id': user_id,
                'count': newNumber
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(JSON.stringify(data)); // Display data in an console.log dialog
        })
        .catch(error => {
            console.error('There was a problem with the fetch request:', error);
        });
    };
}

function reset() {
    const numberText = document.getElementById("count").innerText;
    const intNumber = parseInt(numberText);
    document.getElementById("count").innerText = 0;

    fetch(`${API_DOMAIN}/api/tasbih/update/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'user_id': user_id,
            'count': 0
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(JSON.stringify(data)); // Display data in an console.log dialog
    })
    .catch(error => {
        console.error('There was a problem with the fetch request:', error);
    });
}

function changeMode() {
    const max_count = document.getElementById("max-count");
    const int_max = parseInt(max_count.innerText);
    var mode = 0;

    if (int_max === 33) {
        max_count.innerText = "99";
        var mode = mode + 99;
    } else if (int_max === 99) {
        max_count.innerText = "999999";
        max_count.style.display = "none";
        var mode = mode + 999999;
    } else {
        max_count.innerText = "33";
        max_count.style.display = "block";
        var mode = mode + 33;
    }
    
    fetch(`${API_DOMAIN}/api/tasbih-mode/update/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'user_id': user_id,
            'mode': mode
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(JSON.stringify(data)); // Display data in an console.log dialog
    })
    .catch(error => {
        console.error('There was a problem with the fetch request:', error);
    });
}

