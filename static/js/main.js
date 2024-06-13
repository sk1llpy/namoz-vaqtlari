let API_DOMAIN = 'https://77ef-213-230-102-105.ngrok-free.app';
let tg = window.Telegram.WebApp;

tg.expand();

const urlParams = new URLSearchParams(window.location.search);
const userId = urlParams.get('user_id');

if (userId === null) {
    var user_id = tg.initDataUnsafe.user.id;
} else {
    var user_id = userId;
    var link = document.getElementById('tasbih_a');
    link.href = `${API_DOMAIN}?user_id=${user_id}`;

    var link_zikr = document.getElementById('zikr_a');
    link_zikr.href = `${API_DOMAIN}/main?user_id=${user_id}`;

    var link_home = document.getElementById('home_a');
    link_home.href = `${API_DOMAIN}/main?user_id=${user_id}`;
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
    let region = JSON.stringify(data.region);
    document.getElementById("region-user").innerText = ` ${region.slice(1, -1)}`;

    fetch(`${API_DOMAIN}/api/prayer-times/day/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'region': region.slice(1, -1)
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        let tong = JSON.stringify(data.data.times.tong_saharlik);
        let quyosh = JSON.stringify(data.data.times.quyosh);
        let peshin = JSON.stringify(data.data.times.peshin);
        let asr = JSON.stringify(data.data.times.asr);
        let shom = JSON.stringify(data.data.times.shom_iftor);
        let xufton = JSON.stringify(data.data.times.hufton);

        document.getElementById("prayer-time-tong").innerText = ` ${tong.slice(1, -1)}`;
        document.getElementById("prayer-time-quyosh").innerText = ` ${quyosh.slice(1, -1)}`;
        document.getElementById("prayer-time-peshin").innerText = ` ${peshin.slice(1, -1)}`;
        document.getElementById("prayer-time-asr").innerText = ` ${asr.slice(1, -1)}`;
        document.getElementById("prayer-time-shom").innerText = ` ${shom.slice(1, -1)}`;
        document.getElementById("prayer-time-xufton").innerText = ` ${xufton.slice(1, -1)}`;
    })
    .catch(error => {
        console.error('There was a problem with the fetch request:', error);
    });
})
.catch(error => {
    console.error('There was a problem with the fetch request:', error);
});


