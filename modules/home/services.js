'use strict';

angular.module('Home')

.factory('HomeService',
    ['$http', '$cookieStore', '$rootScope', '$timeout',
    function ($http, $cookieStore, $rootScope, $timeout) {
        var service = {};

		service.renew_token = function (callback) {

			$http.get('http://billeasy.razzatech.com/api/handler.py/renew_token?token='+localStorage.getItem("token"))
			.success(function (response) {
                callback(response);
			});
        };

		service.fetch_accounts = function (callback) {

			$http.get('http://billeasy.razzatech.com/api/handler.py/fetch_billing_accounts?token='+localStorage.getItem("token"))
			.success(function (response) {
                callback(response);
			});
        };

        return service;
    }])

