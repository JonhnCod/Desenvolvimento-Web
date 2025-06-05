import firebase from 'firebase/app';
import 'firebase/firestore';
import 'firebase/auth'

const firebaseConfig = {
    apiKey: "AIzaSyALolyW5bDhFa-wZMW0vvF05RHiqpoF-Zc",
    authDomain: "somativa-final-1a334.firebaseapp.com",
    projectId: "somativa-final-1a334",
    storageBucket: "somativa-final-1a334.firebasestorage.app",
    messagingSenderId: "1057315445812",
    appId: "1:1057315445812:web:610bc862661f16ab95fe61"
  };

if(!firebase.apps.length){
    firebase.initializeApp(firebaseConfig);
}

export default firebase;