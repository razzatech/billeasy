'use strict';

angular.module('Admin')

.factory('AdminService',
    ['$http', '$cookieStore', '$rootScope', '$timeout',
    function ($http, $cookieStore, $rootScope, $timeout) {
        var service = {};

        service.renew_token = function (callback) {
			$http.get('http://billeasy.razzatech.com/api/handler.py/renew_token?token='+localStorage.getItem("token"))
			.success(function (response) {
                callback(response);
			});
        };
		
        return service;
    }])

