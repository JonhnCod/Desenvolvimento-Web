import firebase from 'firebase/app';
import'firebase/firestore';


let firebaseConfig = {
    apiKey: "AIzaSyAtZBwtxxjLaCERboX_g6Rxlar4KS68JWI",
    authDomain: "projeto-web-6a497.firebaseapp.com",
    projectId: "projeto-web-6a497",
    storageBucket: "projeto-web-6a497.firebasestorage.app",
    messagingSenderId: "468208868341",
    appId: "1:468208868341:web:4aec1ca899aa289819debc"
};

if (!firebase.apps.length){
    firebase.initializeApp(firebaseConfig);
}

export default firebase;