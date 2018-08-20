# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from dota.items import DotaMaxItem


class DotamaxSpider(scrapy.Spider):
	name = 'dotamax'
	allowed_domains = ['dotamax.com']
	start_urls = ['http://dotamax.com/']

	def start_requests(self):
		base_url = 'http://www.dotamax.com/player/match/'
		for steam_id in self.settings.get('STEAM_ID'):
			url = base_url + str(steam_id) + '/'
			yield scrapy.Request(url=url, headers=self.settings.get('DEFAULT_REQUEST_HEADERS'),
			                     cookies=self.settings.get('COOKIE'))

	def parse(self, response):
		"""
		用于解析个人用户页的所有比赛
		:param response:
		:return:
		"""
		player_match_node = response.css('.table-player-detail tr')
		for player_match_list in player_match_node:
			match_url = 'http://dotamax.com' + player_match_list.css('td:nth-child(1) > a::attr(href)').extract_first()
			yield scrapy.Request(url=match_url, headers=self.settings.get('DEFAULT_REQUEST_HEADERS'),
			                     cookies=self.settings.get('COOKIE'), callback=self.parse_match_detail_radiant)

		next_url_nodes = response.css('.filterbox div')
		for next_url_node in next_url_nodes:
			if next_url_node.css('::text').extract_first() == '>':
				next_url = next_url_node.css('::attr(onclick)').extract_first().replace("DoNav('", '').replace("')", '')
				yield scrapy.Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

	def parse_match_detail_radiant(self, response):
		dotamax_item = DotaMaxItem()
		match_id = response.css('.match-detail-info.new-box > tr:nth-child(2) > td:nth-child(1)::text').extract_first()
		end_time = response.css('.match-detail-info.new-box > tr:nth-child(2) > td:nth-child(2)::text').extract_first()
		game_length = response.css(
			'.match-detail-info.new-box > tr:nth-child(2) > td:nth-child(3)::text').extract_first()
		match_area = response.css(
			'.match-detail-info.new-box > tr:nth-child(2) > td:nth-child(4)::text').extract_first()
		first_blood = response.css(
			'.match-detail-info.new-box > tr:nth-child(2) > td:nth-child(5)::text').extract_first()
		match_level = response.css(
			'.match-detail-info.new-box > tr:nth-child(2) > td:nth-child(6) font::text').extract_first()
		match_type = response.css(
			'.match-detail-info.new-box > tr:nth-child(2) > td:nth-child(7)::text').extract_first()
		player_camp = response.css('.radiant::text').extract_first('未知').strip()  # 玩家阵营
		is_win = response.css('.radiant font::text').extract_first('失败').replace('(', '').replace(')', '')
		player_nodes = response.css('.table-match-detail-ra tr')
		for player_node in player_nodes:
			player_id = player_node.css('td:nth-child(2) a::attr(href)').extract_first('未知').replace('/player/detail/',
			                                                                                         '')
			player_name = player_node.css('td:nth-child(2) a::text').extract_first('未知').strip()
			player_hero = player_node.css('td:nth-child(3) a::attr(href)').extract_first('未知').replace('/hero/detail/',
			                                                                                           '')
			is_mvp = player_node.css('td:nth-child(3) span::text').extract_first('否')
			hero_level = player_node.css('td:nth-child(3) a::text').extract_first('未知').strip()
			kda = player_node.css('td:nth-child(4) div::text').extract_first('未知')
			kda_detail = player_node.css('td:nth-child(4)::text').extract_first('未知').strip()
			war_rate = player_node.css('td:nth-child(5)::text').extract_first()  # 参加率
			damage_perc = player_node.css('td:nth-child(6)::text').extract_first()  # 伤害占比
			dps = player_node.css('td:nth-child(7)::text').extract_first()  # 伤害数值
			last_deny_hit = player_node.css('td:nth-child(8)::text').extract_first()  # 补刀数
			exp_pm = player_node.css('td:nth-child(9)::text').extract_first()  # 经验
			money_pm = player_node.css('td:nth-child(10)::text').extract_first()  # 金钱
			damage_build = player_node.css('td:nth-child(11)::text').extract_first()  # 建筑伤害
			milk = player_node.css('td:nth-child(12)::text').extract_first()  # 治疗

			# print(match_id, end_time, game_length, match_area, first_blood, match_level, match_type, player_camp,
			#       is_win, player_id, player_name, player_hero, is_mvp, hero_level, kda, kda_detail, war_rate,
			#       damage_perc, dps, last_deny_hit, exp_pm, money_pm, damage_build, milk)

			dotamax_item['match_id'] = match_id
			dotamax_item['end_time'] = end_time
			dotamax_item['game_length'] = game_length
			dotamax_item['match_area'] = match_area
			dotamax_item['first_blood'] = first_blood
			dotamax_item['match_level'] = match_level
			dotamax_item['match_type'] = match_type
			dotamax_item['player_camp'] = player_camp
			dotamax_item['is_win'] = is_win
			dotamax_item['player_id'] = player_id
			dotamax_item['player_name'] = player_name
			dotamax_item['player_hero'] = player_hero
			dotamax_item['is_mvp'] = is_mvp
			dotamax_item['hero_level'] = hero_level
			dotamax_item['kda'] = kda
			dotamax_item['kda_detail'] = kda_detail
			dotamax_item['war_rate'] = war_rate
			dotamax_item['damage_perc'] = damage_perc
			dotamax_item['dps'] = dps
			dotamax_item['last_deny_hit'] = last_deny_hit
			dotamax_item['exp_pm'] = exp_pm
			dotamax_item['money_pm'] = money_pm
			dotamax_item['damage_build'] = damage_build
			dotamax_item['milk'] = milk
			yield dotamax_item

		player_camp = response.css('.dire::text').extract_first('未知').strip()  # 玩家阵营
		is_win = response.css('.dire font::text').extract_first('失败').replace('(', '').replace(')', '')
		player_nodes = response.css('.table-match-detail-dire tr')
		for player_node in player_nodes:
			player_id = player_node.css('td:nth-child(2) a::attr(href)').extract_first('未知').replace('/player/detail/',
			                                                                                         '')
			player_name = player_node.css('td:nth-child(2) a::text').extract_first('未知').strip()
			player_hero = player_node.css('td:nth-child(3) a::attr(href)').extract_first('未知').replace('/hero/detail/',
			                                                                                           '')
			is_mvp = player_node.css('td:nth-child(3) span::text').extract_first('否')
			hero_level = player_node.css('td:nth-child(3) a::text').extract_first('未知').strip()
			kda = player_node.css('td:nth-child(4) div::text').extract_first('未知')
			kda_detail = player_node.css('td:nth-child(4)::text').extract_first('未知').strip()
			war_rate = player_node.css('td:nth-child(5)::text').extract_first()  # 参加率
			damage_perc = player_node.css('td:nth-child(6)::text').extract_first()  # 伤害占比
			dps = player_node.css('td:nth-child(7)::text').extract_first()  # 伤害数值
			last_deny_hit = player_node.css('td:nth-child(8)::text').extract_first()  # 补刀数
			exp_pm = player_node.css('td:nth-child(9)::text').extract_first()  # 经验
			money_pm = player_node.css('td:nth-child(10)::text').extract_first()  # 金钱
			damage_build = player_node.css('td:nth-child(11)::text').extract_first()  # 建筑伤害
			milk = player_node.css('td:nth-child(12)::text').extract_first()  # 治疗

			# print(match_id, end_time, game_length, match_area, first_blood, match_level, match_type, player_camp,
			#       is_win, player_id, player_name, player_hero, is_mvp, hero_level, kda, kda_detail, war_rate,
			#       damage_perc, dps, last_deny_hit, exp_pm, money_pm, damage_build, milk)

			dotamax_item['match_id'] = match_id
			dotamax_item['end_time'] = end_time
			dotamax_item['game_length'] = game_length
			dotamax_item['match_area'] = match_area
			dotamax_item['first_blood'] = first_blood
			dotamax_item['match_level'] = match_level
			dotamax_item['match_type'] = match_type
			dotamax_item['player_camp'] = player_camp
			dotamax_item['is_win'] = is_win
			dotamax_item['player_id'] = player_id
			dotamax_item['player_name'] = player_name
			dotamax_item['player_hero'] = player_hero
			dotamax_item['is_mvp'] = is_mvp
			dotamax_item['hero_level'] = hero_level
			dotamax_item['kda'] = kda
			dotamax_item['kda_detail'] = kda_detail
			dotamax_item['war_rate'] = war_rate
			dotamax_item['damage_perc'] = damage_perc
			dotamax_item['dps'] = dps
			dotamax_item['last_deny_hit'] = last_deny_hit
			dotamax_item['exp_pm'] = exp_pm
			dotamax_item['money_pm'] = money_pm
			dotamax_item['damage_build'] = damage_build
			dotamax_item['milk'] = milk
			yield dotamax_item
