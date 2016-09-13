'use strict';

// declare modules
angular.module('Authentication', []);
angular.module('SignUp', []);
angular.module('Home', []);
angular.module('History', []);
angular.module('Enrollment', []);
angular.module('Admin', []);
angular.module('Merchants', []);
angular.module('NewMerchant', []);
angular.module('Bills', []);

angular.module('BasicHttpAuthExample', [
    'Authentication',
    'SignUp',
    'Home',
	'History',
	'Enrollment',
    'Admin',
	'Merchants',
	'NewMerchant',
	'Bills',
    'ngRoute',
    'ngCookies'
])

.config(['$routeProvider', function ($routeProvider) {

    $routeProvider
        .when('/login', {
            controller: 'LoginController',
            templateUrl: '/modules/login/login.html'
        })

		.when('/signup', {
            controller: 'SignUpController',
            templateUrl: '/modules/signup/signup.html'
        })

		.when('/home', {
            controller: 'HomeController',
            templateUrl: '/modules/home/home.html'
        })
		
		.when('/history', {
            controller: 'HistoryController',
            templateUrl: '/modules/history/history.html'
        })

        .when('/enrollment', {
            controller: 'EnrollmentController',
            templateUrl: '/modules/enrollment/enrollment.html'
        })

		.when('/admin', {
            controller: 'AdminController',
            templateUrl: '/modules/admin/admin.html'
        })
		
		.when('/merchants', {
            controller: 'MerchantsController',
            templateUrl: '/modules/merchants/merchants.html'
        })
		
		.when('/new_merchant', {
            controller: 'NewMerchantController',
            templateUrl: '/modules/new_merchant/new_merchant.html'
        })
		
        .when('/bills', {
            controller: 'BillsController',
            templateUrl: '/modules/bills/bills.html'
        })
		
		.when('/bills_csv_uploaded', {
            controller: 'BillsController',
            templateUrl: '/modules/bills/bills.html'
        })
		
        .otherwise({ redirectTo: '/login' });
}])

.run(['$rootScope', '$location', '$cookieStore', '$http',
    function ($rootScope, $location, $cookieStore, $http) {
        $rootScope.$on('$locationChangeStart', function (event, next, current) {


            if($location.path() === '/merchants')
            {

            }
			else if($location.path() === '/bills')
            {

            }
			else if($location.path() === '/bills_csv_uploaded')
            {
				alert("CSV file uploaded.");
				$location.path('/bills');
            }
			else if($location.path() === '/new_merchant')
            {

            }
			else if($location.path() === '/history')
            {

            }
            else if($location.path() === '/enrollment')
            {
				
            }
			else if($location.path() === '/password_reset')
            {
				alert("Your password has been reset.");
            }
			else if($location.path() === '/signup')
            {
				console.log("loading captcha...");
				setTimeout(function()
				{
					grecaptcha.render("recaptcha", {
						sitekey: '6Lfp5SkTAAAAALxSLN1git8Bhsmz0iStm8kw1pb_',
					});
					console.log("captcha ready.")
				}, 500);
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