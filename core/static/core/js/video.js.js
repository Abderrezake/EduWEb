document.addEventListener('DOMContentLoaded', function () {
    const arrow = document.getElementById('arrow');
    const arrowIcon = document.getElementById('arrowIcon');
    const comments = document.getElementById('comments');

    arrow.addEventListener('click', function () {
        if (comments.style.display === 'block' || comments.style.display === '') {
            comments.style.display = 'none';
            arrowIcon.innerText = 'expand_more';
        } else {
            comments.style.display = 'block';
            arrowIcon.innerText = 'expand_less';
        }
    });
});


document.addEventListener("DOMContentLoaded", function() {
    // Sélectionnez toutes les vidéos dans la liste de lecture
    const playlistVideos = document.querySelectorAll('.video-playlist .video');

    // Parcourez chaque vidéo et ajoutez un gestionnaire d'événements clic
    playlistVideos.forEach(function(video) {
        video.addEventListener('click', function() {
            // Récupérez l'attribut data-id pour obtenir l'identifiant de la vidéo
            const videoId = this.getAttribute('data-id');

            // Obtenez la vidéo principale
            const mainVideo = document.querySelector('.main-video video');

            // Mettez à jour la source vidéo de la vidéo principale en fonction de l'identifiant de la vidéo sélectionnée
            switch (videoId) {
                case 'a1':
                    mainVideo.src = 'img/cour.mp4'; // Remplacez ceci par le chemin de la nouvelle vidéo
                    break;
                case 'a2':
                    mainVideo.src = 'img/cour.mp4'; // Remplacez ceci par le chemin de la nouvelle vidéo
                    break;

                // Ajoutez des cas pour les autres vidéos de la liste de lecture si nécessaire
            }

            mainVideo.pause();
        });
    });
});

// Sélectionnez toutes les vidéos dans la liste de lecture
const playlistVideos = document.querySelectorAll('.video-playlist .video');

// Parcourez chaque vidéo et ajoutez un gestionnaire d'événements clic
playlistVideos.forEach(function(video) {
    video.addEventListener('click', function() {
        // Supprimez la classe "active" de toutes les vidéos de la liste de lecture
        playlistVideos.forEach(function(video) {
            video.classList.remove('active');
        });

        // Ajoutez la classe "active" à la vidéo sur laquelle vous avez cliqué
        this.classList.add('active');

        // Mettez à jour la source de la vidéo principale en fonction de la vidéo sur laquelle vous avez cliqué
        const videoSrc = this.getAttribute('data-src');
        const mainVideo = document.querySelector('.main-video video');
        mainVideo.src = videoSrc;
    });
});

// Parcourez chaque vidéo et ajoutez un gestionnaire d'événements clic
playlistVideos.forEach(function(video) {
    video.addEventListener('click', function() {
        // Supprimez la classe "active" de toutes les vidéos de la liste de lecture
        playlistVideos.forEach(function(video) {
            video.classList.remove('active');
            // Changez l'icône de lecture en icône de pause pour toutes les vidéos de la liste de lecture
            video.querySelector('img').src = 'img/play.svg';
        });

        // Ajoutez la classe "active" à la vidéo sur laquelle vous avez cliqué
        this.classList.add('active');
        // Changez l'icône de lecture en icône de pause pour la vidéo active
        this.querySelector('img').src = 'img/pause.svg';

        // Mettez à jour la source de la vidéo principale en fonction de la vidéo sur laquelle vous avez cliqué
        const videoSrc = this.getAttribute('data-src');
        const mainVideo = document.querySelector('.main-video video');
        mainVideo.src = videoSrc;
    });
});



