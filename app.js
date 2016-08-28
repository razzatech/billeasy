'use strict';

// declare modules
angular.module('Authentication', []);
angular.module('SignUp', []);
angular.module('Home', []);
angular.module('Admin', []);
angular.module('Enrollment', []);

angular.module('BasicHttpAuthExample', [
    'Authentication',
    'SignUp',
    'Home',
    'Admin',
    'Enrollment',
    'ngRoute',
    'ngCookies'
])

.config(['$routeProvider', function ($routeProvider) {

    $routeProvider
        .when('/login', {
            controller: 'LoginController',
            templateUrl: '/modules/login/login.html',
            hideMenus: true
        })

		.when('/signup', {
            controller: 'SignUpController',
            templateUrl: '/modules/signup/signup.html',
            hideMenus: true
        })

		.when('/home', {
            controller: 'HomeController',
            templateUrl: '/modules/home/home.html'
        })

        .when('/enrollment', {
            controller: 'EnrollmentController',
            templateUrl: '/modules/enrollment/enrollment.html'
        })

		.when('/admin', {
            controller: 'AdminController',
            templateUrl: '/modules/admin/admin.html'
        })

        .when('/admin/all_bills', {
            controller: 'AdminController',
            templateUrl: '/modules/admin/all_bills.html'
        })

        .otherwise({ redirectTo: '/login' });
}])

.run(['$rootScope', '$location', '$cookieStore', '$http',
    function ($rootScope, $location, $cookieStore, $http) {
        $rootScope.$on('$locationChangeStart', function (event, next, current) {


            if($location.path() === '/admin/all_bills')
            {

            }
            else if($location.path() === '/enrollment')
            {

            }
            else if (localStorage.getItem("token")!=null) {
				if(localStorage.getItem("admin")) {
					$location.path('/admin');
				}
				else {
					$location.path('/home');
				}
            }

            /*
            if (localStorage.getItem("token")!=null) {
				if(localStorage.getItem("admin")) {
					$location.path('/admin');
				}
				else {
					$location.path('/home');
				}
            } else if ($location.path() === '/login' || $location.path() === '/signup') {

			} else{
				$location.path('/login');
				console.log("No login data found. Redirecting to login page.");
			}
			*/

        });
    }]);