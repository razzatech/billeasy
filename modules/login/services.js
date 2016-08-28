'use strict';

angular.module('Authentication')

.factory('AuthenticationService',
    ['$http', '$cookieStore', '$rootScope', '$timeout',
    function ($http, $cookieStore, $rootScope, $timeout) {
        var service = {};

        service.Login = function (user_name_or_email, password, callback) {
                $http.post('http://billeasy.razzatech.com/api/_.py/log_in', { user_name_or_email: user_name_or_email, password: password }, {headers : {'Content-Type': 'x-www-form-urlencoded'}})
			.success(function (response) {
                        if(!response.success) {
                                response.message = 'User name or password is incorrect';
                         }
                        callback(response);
                });
        };

        return service;
    }])

