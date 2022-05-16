const gulp = require('gulp');
const sass = require('gulp-sass');
const browserSync = require('browser-sync').create();

const paths = {
    default: './',
    sass: {
        src: './scss/**/*.scss',
        dest: './css'
    },
    html: './*.html',
    js: './js/**/*.js'

    /*,
    minify: {
        src: './css/*.css',
        dest: './css'
    }
    */
};

function style(){
    //Where is my SCSS file?
    return gulp.src('scss/main.scss')

    //Pass that file through SASS compiler
    .pipe(sass().on('error', sass.logError))

    //Where do I save the compiled CSS?
    .pipe(gulp.dest(paths.sass.dest))

    //Stream changes across all browsers
    .pipe(browserSync.stream());
}

function watch(){
    browserSync.init({
        server:{
            baseDir: paths.default,
            notify: false,
            open: true
        }
    });
    gulp.watch(paths.sass.src, style);
    gulp.watch(paths.html).on('change', browserSync.reload);
    gulp.watch(paths.js).on('change', browserSync.reload);
}

exports.style = style;
exports.watch = watch;