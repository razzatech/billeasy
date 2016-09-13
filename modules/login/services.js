'use strict';

angular.module('Authentication')

.factory('AuthenticationService',
    ['$http', '$cookieStore', '$rootScope', '$timeout',
    function ($http, $cookieStore, $rootScope, $timeout) {
        var service = {};

        service.Login = function (user_name_or_email, password, callback) {
                $http.post('http://billeasy.razzatech.com/api/handler.py/log_in', { user_name_or_email: user_name_or_email, password: password }, {headers : {'Content-Type': 'x-www-form-urlencoded'}})
			.success(function (response) {
                        if(!response.success) {
                                response.message = 'User name or password is incorrect';
                         }
                        callback(response);
                });
        };
		
		service.forgot_password = function (user_name_or_email, callback) {

			$http.get('http://billeasy.razzatech.com/api/handler.py/forgot_password?user_name_or_email='+user_name_or_email)
			.success(function (response) {
                callback(response);
			});
        };

        return service;
    }])

