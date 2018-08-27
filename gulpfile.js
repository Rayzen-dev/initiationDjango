const gulp = require('gulp'),
    sass = require('gulp-ruby-sass'),
    cleanCSS = require('gulp-clean-css')
    publicPath = './static/'
;

gulp.task('sass', () => {
    return sass('static/scss/*.scss')
        .on('error', sass.logError)
        .pipe(gulp.dest('static/css'))
});

gulp.task('compressCSS', ['sass'], () => {
    return gulp.src('static/css/*.css')
        .pipe(cleanCSS({compatibility:'ie8'}))
        .pipe(gulp.dest('static/css'))
});

gulp.task('default', ['compressCSS'], () => {});

gulp.task('watch', () => {
    gulp.watch(publicPath + 'scss/*.scss', ['compressCSS']);
});
